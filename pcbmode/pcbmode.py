#!/usr/bin/python

import os
import json
import argparse

from os import getcwd as getcwd

from pkg_resources import resource_filename, resource_exists

# PCBmodE modules
from pcbmode.config import config
from pcbmode.utils import utils
from pcbmode.utils import gerber
from pcbmode.utils import extract
from pcbmode.utils import excellon
from pcbmode.utils import messages as msg
from pcbmode.utils import bom
from pcbmode.utils import coord_file
from pcbmode.utils.board import Board


def cmdArgSetup(pcbmode_version):
    """
    Sets up the commandline arguments form and variables
    """

    description = "PCBmodE is a script-based PCB design tool that generates SVG files from JSON inpus files. It can then convert the SVG into Gerbers. Viewing and (some) editing is done with Inkscape. You can support this project here: https://github.com/sponsors/saardrimer "

    epilog = """
    """
    
    # commandline argument settings and parsing
    argp = argparse.ArgumentParser(description=description, 
                      add_help=True, epilog=epilog)
     
    argp.add_argument('-b', '--board-name',
                      dest='boards', required=True, nargs=1,
                      help='The name of the board. The location of the files should be specified in the configuration file, otherwise defaults are used')
     
    argp.add_argument('-f', '--filein', required=False,
                      dest='filein',
                      help='Input file name')
     
    argp.add_argument('-o', '--fileout',
                      dest='fileout',
                      help='Output file name')
     
    argp.add_argument('-c', '--config-file', default='pcbmode_config.json',
                      dest='config_file',
                      help='Configuration file name (default=pcbmode_config.json)')
     
    argp.add_argument('-m', '--make-board',
                      action='store_true', dest='make', default=False,
                      help="Create SVG for the board specified with the '-b'/'--board_name' switch. The output's location can be specified in the configuration file")
     
    argp.add_argument('-e', '--extract',
                      action='store_true', dest='extract', default=False,
                      help="Extract routing and component placement from board's SVG")

    argp.add_argument('--extract-refdefs',
                      action='store_true', dest='extract_refdefs', default=False,
                      help="Extract components' reference designator location and rotation from board's SVG")
     
    argp.add_argument('--fab', nargs='?',
                      dest='fab', default=False,
                      help='Generate manufacturing files (Gerbers, Excellon, etc.) An optional argument specifies the fab for custom filenames')

    argp.add_argument('-p', '--make-pngs',
                      action='store_true', dest='pngs', default=False,
                      help='Generate a PNG of the board (requires Inkscape)')

    argp.add_argument('--no-layer-index',
                      action='store_true', dest='no_layer_index', default=False,
                      help='Do not add a layer index to SVG')

    argp.add_argument('--no-drill-index',
                      action='store_true', dest='no_drill_index', default=False,
                      help='Do not add a drill index to SVG')

    argp.add_argument('--no-flashes',
                      action='store_true', dest='no_flashes', default=False,
                      help='Do not add pad flashes to Gerbers')

    argp.add_argument('--no-docs',
                      action='store_true', dest='no_docs', default=False,
                      help='Do not add documentation')

    argp.add_argument('--renumber-refdefs', nargs='?',
                      dest='renumber', default=False,
                      help="Renumber refdefs (valid options are 'top-to-bottom' (default), 'bottom-to-top', 'left-to-right', 'right-to-left'")

    argp.add_argument('--make-coord-file', nargs='?',
                      dest='coord_file', default=False,
                      help="Create a simple placement coordinate CSV file")

    argp.add_argument('--make-bom', nargs='?',
                      dest='make_bom', default=False, 
                      help='Create a bill of materials')

    return argp




def load_pcbmode_config():
    """
    Load the default and local configuration files into memory
    """

    pcbmode_file = os.path.realpath(__file__)    # Get location of pcbmode.py
    pcbmode_path = os.path.dirname(pcbmode_file) # Get only the path
    config_path = 'config'
    config_filename = 'pcbmode_config.json'
    config.cfg = utils.dictFromJsonFile(os.path.join(pcbmode_path,
                                                     config_path,
                                                     config_filename))


def load_board_config():
    """
    Load the board's configuration data
    """

    filename = os.path.join(config.cfg['locations']['boards'], 
                            config.cfg['name'], 
                            config.cfg['name'] + '.json')
    config.brd = utils.dictFromJsonFile(filename)

    tmp_dict = config.brd.get('config')

    if tmp_dict != None:
        config.brd['config']['units'] = tmp_dict.get('units', 'mm') or 'mm'
        config.brd['config']['style-layout'] = tmp_dict.get('style-layout', 'default') or 'default'
    else:
        config.brd['config'] = {}
        config.brd['config']['units'] = 'mm'
        config.brd['config']['style-layout'] = 'default'



def load_style():
    """
    """

    layout_style = config.brd['config']['style-layout']
    layout_style_filename = 'layout.json'
    paths = [os.path.join(config.cfg['base-dir'],
                          config.cfg['locations']['styles'],
                          layout_style, layout_style_filename)] # project dir

    style_resource = (__name__, '/'.join(['styles', layout_style, layout_style_filename]))
    if resource_exists(*style_resource):
        paths.append(resource_filename(*style_resource))

    filenames = ''
    for path in paths:
        filename = path
        filenames += "  %s \n" % filename
        if os.path.isfile(filename):
            config.stl['layout'] = utils.dictFromJsonFile(filename)
            break

    if not 'layout' in config.stl or config.stl['layout'] == {}:
        msg.error("Couldn't find style file %s. Looked for it here:\n%s" % (layout_style_filename, filenames))



def load_stackup():
    """
    """

    try:
        stackup_filename = config.brd['stackup']['name'] + '.json'
    except:
        stackup_filename = 'two-layer.json'

    paths = [os.path.join(config.cfg['base-dir'], config.cfg['locations']['stackups'], stackup_filename)] # project dir

    stackup_resource = (__name__, '/'.join(['stackups', stackup_filename]))
    if resource_exists(*stackup_resource):
        paths.append(resource_filename(*stackup_resource))

    filenames = ''
    for path in paths:
        filename = path
        filenames += "  %s \n" % filename
        if os.path.isfile(filename):
            config.stk = utils.dictFromJsonFile(filename)
            break

    if config.stk == {}:
        msg.error("Couldn't find stackup file %s. Looked for it here:\n%s" % (stackup_filename, filenames))

    config.stk['layers-dict'], config.stk['layer-names'] = utils.getLayerList()
    config.stk['surface-layers'] = [config.stk['layers-dict'][0], config.stk['layers-dict'][-1]]
    config.stk['internal-layers'] = config.stk['layers-dict'][1:-1]
    config.stk['surface-layer-names'] = [config.stk['layer-names'][0], config.stk['layer-names'][-1]]
    config.stk['internal-layer-names'] = config.stk['layer-names'][1:-1]



def load_cache():
    """
    """

    filename = os.path.join(config.cfg['locations']['boards'], 
                            config.cfg['name'],
                            config.cfg['locations']['build'],
                            'paths_db.json')

    if os.path.isfile(filename):
        config.pth = utils.dictFromJsonFile(filename)



def load_routing():
    """
    """

    filename = os.path.join(config.cfg['base-dir'], 
                            config.brd['files'].get('routing-json') or config.cfg['name'] + '_routing.json')

    if os.path.isfile(filename):
        config.rte = utils.dictFromJsonFile(filename)




def make_config(name, version, cmdline_args):
    """
    """

    # namespace URLs
    config.cfg['ns'] = {
        None       : "http://www.w3.org/2000/svg",
        "dc"       : "http://purl.org/dc/elements/1.1/",
        "cc"       : "http://creativecommons.org/ns#",
        "rdf"      : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "svg"      : "http://www.w3.org/2000/svg",
        "sodipodi" : "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        "inkscape" : "http://www.inkscape.org/namespaces/inkscape",
        # Namespace URI are strings; they don't need to be URLs. See:
        #  http://en.wikipedia.org/wiki/XML_namespace
        "pcbmode"  : "pcbmode"
    }
    config.cfg['namespace'] = config.cfg['ns']


    #------------------------------------------------------------------
    # Distances
    #------------------------------------------------------------------
    # If any of the distance definitions are missing from the board's
    # configuration file, use PCBmodE's defaults
    #------------------------------------------------------------------
    config_distances_dict = config.cfg['params']['distances']
    try:
        board_distances_dict = config.brd['params']['distances']
    except:
        board_distances_dict = {}

    distance_keys = ['from-pour-to', 'soldermask', 'solderpaste']

    for dk in distance_keys:
        config_dict = config_distances_dict[dk]
        try:
            board_dict = board_distances_dict[dk]
        except:
            board_distances_dict[dk] = {}
            board_dict = board_distances_dict[dk]
        
        for k in config_dict.keys():
            board_dict[k] = (board_dict.get(k) or config_dict[k])


    #-----------------------------------------------------------------
    # Commandline overrides
    #-----------------------------------------------------------------
    # These are stored in a temporary dictionary so that they are not
    # written to the config file when the board's configuration is
    # dumped, with extraction, for example
    #-----------------------------------------------------------------
    config.tmp = {}
    config.tmp['no-layer-index'] = (cmdline_args.no_layer_index or
                                    config.brd['config'].get('no-layer-index') or
                                    False)
    config.tmp['no-flashes'] = (cmdline_args.no_flashes or
                                config.brd['config'].get('no-flashes') or
                                False)
    config.tmp['no-docs'] = (cmdline_args.no_docs or
                             config.brd['config'].get('no-docs') or
                             False)
    config.tmp['no-drill-index'] = (cmdline_args.no_drill_index or
                                    config.brd['config'].get('no-drill-index') or
                                    False)


    # Define Gerber setting from board's config or defaults
    try:
        tmp = config.brd['gerber']
    except:
        config.brd['gerber'] = {}
    gd = config.brd['gerber']    
    gd['decimals'] = config.brd['gerber'].get('decimals') or 6
    gd['digits'] = config.brd['gerber'].get('digits') or 6
    gd['steps-per-segment'] = config.brd['gerber'].get('steps-per-segment') or 100
    gd['min-segment-length'] = config.brd['gerber'].get('min-segment-length') or 0.05

    # Inkscape inverts the 'y' axis for some historical reasons.
    # This means that we need to invert it as well. This should
    # be the only place this inversion happens so it's easy to
    # control if things change.
    config.cfg['invert-y'] = -1


    #-----------------------------------------------------------------
    # Commandline overrides
    #-----------------------------------------------------------------
    # Controls the visibility of layers and whether they are locked by
    # default. This is the "master" control; settings in the board's
    # config file will override these settings
    #-----------------------------------------------------------------
    layer_control_default = {
      "conductor": { 
        "place": True, "hide": False, "lock": False, 
        "pours": { "place": True, "hide": False, "lock": True },
        "pads": { "place": True, "hide": False, "lock": False },
        "routing": { "place": True, "hide": False, "lock": False }
      },
      "soldermask": { "place": True, "hide": False, "lock": False },
      "solderpaste": { "place": True, "hide": True, "lock": True },
      "silkscreen": { "place": True, "hide": False, "lock": False },
      "assembly": { "place": True, "hide": False, "lock": False },
      "documentation": { "place": True, "hide": False, "lock": False },
      "dimensions": { "place": True, "hide": False, "lock": True },
      "origin": { "place": True, "hide": False, "lock": True },
      "drills": { "place": True, "hide": False, "lock": False },
      "placement": { "place": True, "hide": False, "lock": False },
      "outline": { "place": True, "hide": False, "lock": True }
    }

    # Get overrides
    layer_control_config = config.brd.get('layer-control')
    if layer_control_config != None:
        # Python2
        #config.brd['layer-control'] = dict(layer_control_default.items() +
        #                                   layer_control_config.items())
        
        # Python3
        config.brd['layer-control'] = {**layer_control_default, **layer_control_config}
        

    else:
        config.brd['layer-control'] = layer_control_default


    return





def main():

    # Info while in development
    msg.info("Important!")
    msg.info("You are using a version of PCBmodE ('cinco') that's actively under development.")
    msg.info("Please support this project at https://github.com/sponsors/saardrimer.\n")

    # Get PCBmodE version
    version = utils.get_git_revision()

    # Setup and parse commandline arguments
    argp = cmdArgSetup(version)
    cmdline_args = argp.parse_args()

    # Might support running multiple boards in the future,
    # for now get the first onw
    board_name = cmdline_args.boards[0]

    msg.info("Loading PCBmodE's configuration data")
    load_pcbmode_config()

    # Add more config
    config.cfg['name'] = board_name
    config.cfg['version'] = version
    config.cfg['base-dir'] = os.path.join(config.cfg['locations']['boards'], board_name)

    config.cfg['digest-digits'] = 10

    msg.info("Loading board's configuration data")
    load_board_config()

    load_style()
    load_stackup()
    load_cache()
    load_routing()

    make_config(board_name, version, cmdline_args)

    # Check if build directory exists; if not, create
    build_dir = os.path.join(config.cfg['base-dir'], config.cfg['locations']['build'])
    utils.create_dir(build_dir)

    # Renumber refdefs and dump board config file
    if cmdline_args.renumber is not False:
        msg.info("Renumbering refdefs")
        if cmdline_args.renumber is None:
            order = 'top-to-bottom'
        else:
            order = cmdline_args.renumber.lower()    

        utils.renumberRefdefs(order)

    # Extract information from SVG file
    elif cmdline_args.extract is True or cmdline_args.extract_refdefs is True:
        extract.extract(extract=cmdline_args.extract,
                        extract_refdefs=cmdline_args.extract_refdefs)

    # Create a BoM
    elif cmdline_args.make_bom is not False:
        bom.make_bom(cmdline_args.make_bom)

    elif cmdline_args.coord_file is not False:
        coord_file.makeCoordFile(cmdline_args.coord_file)

    else:
        # Make the board
        if cmdline_args.make is True:
            msg.info("Creating board")
            board = Board()

        # Create production files (Gerbers, Excellon, etc.)
        if cmdline_args.fab is not False:
            if cmdline_args.fab is None:
                manufacturer = 'default'
            else:
                manufacturer = cmdline_args.fab.lower()
     
            msg.info("Creating Gerbers")
            gerber.gerberise(manufacturer)

            msg.info("Creating excellon drill file")
            excellon.makeExcellon(manufacturer)
     
        if cmdline_args.pngs is True:
            msg.info("Creating PNGs")
            utils.makePngs()
   
    
    filename = os.path.join(config.cfg['locations']['boards'], 
                            config.cfg['name'],
                            config.cfg['locations']['build'],
                            'paths_db.json')

    try:
        f = open(filename, 'w')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
 
    json.dump(config.pth, f, sort_keys=True, indent=2)
    f.close()

    msg.info("Done!")



if __name__ == "__main__":
    main()
