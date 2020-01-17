#!/usr/bin/python

#!/usr/bin/python

# PCBmodE, a printed circuit design software with a twist
# Copyright (C) 2020 Saar Drimer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import unittest

from pcbmode.utils.svg_path_grammar import get_grammar


class TestSvgPathGrammar(unittest.TestCase):
    """
    Test the SVG path grammar module
    """

    def test_svg_path_grammar(self):

        grammar = get_grammar()
        self.assertIsNotNone(grammar, "should have SVG grammar")

        svg_paths = [
            # M=moveto absolute
            "M 15, -3",
            "M-3,2.0",
            "M 1.2, 3.5",
            "M 3,4 6,5 8 9 10 11",
            # m=moveto relative
            "m 3,0",
            "m1,1",
            " m 7 8",
            "m -1 -2 -3 -4 5 6 7.8 9",
            # C=curveto absolute (cubic bezier)
            "C1,2,3,4,5,6",
            "C 1,2 3,4 5,6",
            "C -1,3.2 5.6,7 8,0.9",
            # c=curveto relative (cubic bezier)
            "c1,2,3,4,5,6",
            "c 1,2 3,4 5,6",
            " c -1,3.2 5.6,7 8,0.9",
            # Q=curveto absolute (quadratic bezier)
            "Q1,2,3,4",
            "Q 1,2 3,4",
            "Q -1,3.2 5.6,7",
            # q=curveto relative (quadratic bezier)
            "q1,2,3,4",
            "q 1,2 3,4",
            " q -1,3.2 5.6,7",
            # T=smooth curveto absolute (quadratic bezier)
            "T 15, -3",
            "T-3,2.0",
            "T 1.2, 3.5",
            # t=smooth curveto relative (quadratic bezier)
            "t 3,0",
            "t1,1",
            " t 7 8",
            # S=smooth curveto absolute
            "S1,2,3,4",
            "S 1,2 3,4",
            "S -1,3.2 5.6,7",
            # s=smooth curveto relative
            "s1,2,3,4",
            "s 1,2 3,4",
            " s -1,3.2 5.6,7",
            # L=lineto absolute
            "L 15, -3",
            "L-3,2.0",
            "L 1.2, 3.5",
            # l=lineto relative
            "l 3,0",
            "l1,1",
            " l 7 8",
            # H=horizontal lineto absolute
            "H 15",
            "H-3.2",
            "H 1.2",
            # h=horizontal lineto relative
            "h 3",
            "h1.1",
            " h 7",
            # V=vertical lineto absolute
            "V 15",
            "V-3.2",
            "V 1.2",
            # v=vertical lineto relative
            "v 3",
            "v1.1",
            " v 7",
            # A=arcto absolute
            #'A20,20 0 0,0 40,40',
            # a=arcto relative
            # z=closepath
            "z",
            "Z",
            "z ",
            # combined
            "M10,10 L20,5 v-10 h-25 z",
            "M10,10L20,5v-10h-25z",
            "M8-29q17-29 12 29q-7 29-23-11t11-17z",
            "M 7.513942,3.475073 7.461022,1.217295 M 6.437967,2.310906 8.413523,2.381466 M -9.9424428,3.192851 -9.9777228,1.14674 m -0.9524982,0.987777 1.9402778,-0.07056 m 8.4174479,10.075407 -0.011616,-1.980354 m -1.4601453,1.980354 c 0,-0.199561 0.00114,-2.03765 0.00114,-2.03765 m 0.1984205,-17.1927271 1.272204,0.02495 m -2.0455043,0.523847 c 0.099783,0 2.6691335,0.074835 2.6691335,0.074835 m -3.7417753,0.4989036 c 0.2743989,0.024946 4.8144173,0.074835 4.8144173,0.074835 m -2.4695713,1.7649136 0.024948,-1.5902972 M -3.017117,10.966942 -1.3474994,9.4474414 0.5250962,11.091668 M -6.6417554,-2.2085415 -7.8231616,-3.4231395 M 4.70829,8.3931495 3.5268836,7.1785515 m 0.2079102,-9.628195 1.2145982,-1.181407 M -4.3581745,10.973764 c 0,-0.123749 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.100319 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z m 5.3632082,0.04989 c 0,-0.123749 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.100319 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z M 1.9280044,-6.1885035 c 0,-0.1237494 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.1003186 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z M 7.316158,0.02284 c 0,-0.123749 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.100319 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z m -0.04989,4.589909 c 0,-0.123749 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.100319 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z M -10.544573,4.063955 c 0,-0.123749 0.100319,-0.224067 0.224068,-0.224067 0.123749,0 0.224068,0.100318 0.224068,0.224067 0,0.12375 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100318 -0.224068,-0.224068 z m 0.02494,-3.791663 c 0,-0.12375 0.100319,-0.224068 0.224068,-0.224068 0.123749,0 0.224068,0.100318 0.224068,0.224068 0,0.123749 -0.100319,0.224068 -0.224068,0.224068 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.224068 z m 0.210711,-0.011607 c 0.6676114,-3.0179015 2.8246219,-5.4760625 5.6604939,-6.5639398 m 6.8001974,0.097835 C 4.787863,-5.1056178 6.799646,-2.8085568 7.507775,0.006422 M 7.459295,4.671796 C 6.621676,7.7287535 4.2390222,10.146929 1.2030826,11.034577 m -5.255073,-0.03226 C -7.2094648,10.036494 -9.6413932,7.4095315 -10.328927,4.140282 m 2.590901,-1.893425 c 0,-3.5166725 2.8508244,-6.3674975 6.3674986,-6.3674985 3.5166739,-2e-6 6.3675024,2.850825 6.3675024,6.3674985 0,3.5166745 -2.8508285,6.3675005 -6.3675024,6.3674995 -3.5166742,0 -6.3674986,-2.850828 -6.3674986,-6.3674995 z m 0.1477197,5.9301355 1.2145986,-1.181406 m 1.5435753,-13.3587062 c 0,-0.1237493 0.100319,-0.2240679 0.224068,-0.2240679 0.123749,0 0.224068,0.1003186 0.224068,0.2240679 0,0.1237492 -0.100319,0.2240682 -0.224068,0.2240682 -0.123749,0 -0.224068,-0.100319 -0.224068,-0.2240682 z",
            "m 16.08082,-7.884302 c 0,-0.07123 0.01592,-0.1371797 0.06229,-0.1835545 0.04637,-0.046369 0.112322,-0.062286 0.183555,-0.062286 h 0.453099 c 0.07123,0 0.137183,0.015917 0.183555,0.062286 0.04637,0.046372 0.06284,0.1123245 0.06284,0.1835545 v 0.4398715 h 1.732469 c 0.07123,0 0.134976,0.017571 0.181351,0.06394 0.04637,0.046369 0.06449,0.1106678 0.06449,0.1819007 v 0.6074381 c 0,0.07123 -0.01812,0.1371826 -0.06449,0.1835545 -0.04637,0.046372 -0.110118,0.062289 -0.181351,0.062289 h -1.732469 v 0.4415225 c 0,0.07123 -0.01647,0.1371797 -0.06284,0.1835545 -0.04637,0.046369 -0.112322,0.06284 -0.183555,0.06284 h -0.453099 c -0.07123,0 -0.13718,-0.01647 -0.183555,-0.06284 -0.04637,-0.046369 -0.06229,-0.1123216 -0.06229,-0.1835545 z m 0,2.6155168 c 0,-0.07123 0.01592,-0.1371797 0.06229,-0.1835545 0.04637,-0.046369 0.112322,-0.06284 0.183555,-0.06284 h 2.431962 c 0.07123,0 0.134976,0.016471 0.181351,0.06284 0.04637,0.046369 0.06449,0.1123217 0.06449,0.1835545 v 0.5820833 c 0,0.07123 -0.01812,0.1371798 -0.06449,0.1835545 -0.04637,0.046369 -0.110118,0.062287 -0.181351,0.062287 h -0.722644 v 0.4045937 h 0.722644 c 0.07123,0 0.134976,0.015917 0.181351,0.062286 0.04637,0.046369 0.06449,0.1123245 0.06449,0.1835545 v 0.5820833 c 0,0.07123 -0.01812,0.1349784 -0.06449,0.1813504 -0.04637,0.046369 -0.110118,0.064493 -0.181351,0.064493 h -2.431962 c -0.07123,0 -0.13718,-0.018124 -0.183555,-0.064493 -0.04637,-0.046369 -0.06229,-0.1101175 -0.06229,-0.1813504 v -0.5820833 c 0,-0.07123 0.01592,-0.1371797 0.06229,-0.1835545 0.04637,-0.046369 0.112322,-0.062286 0.183555,-0.062286 h 0.703351 v -0.4045937 h -0.703351 c -0.07123,0 -0.13718,-0.015917 -0.183555,-0.062287 -0.04637,-0.046369 -0.06229,-0.1123216 -0.06229,-0.1835545 z m 0,2.8492307 c 0,-0.07123 0.01592,-0.1349756 0.06229,-0.1813475 0.04637,-0.046372 0.112322,-0.062289 0.183555,-0.062289 h 2.431962 c 0.07123,0 0.134976,0.015917 0.181351,0.062289 0.04637,0.046369 0.06449,0.1101174 0.06449,0.1813475 v 1.7423919 c 0,0.07123 -0.01812,0.1355287 -0.06449,0.1819007 -0.04637,0.046372 -0.110118,0.064493 -0.181351,0.064493 h -0.439871 c -0.07123,0 -0.13718,-0.018121 -0.183555,-0.064493 -0.04637,-0.046369 -0.06229,-0.1106678 -0.06229,-0.1819007 v -0.9254885 h -0.101422 v 0.6206659 c 0,0.07123 -0.01647,0.1371826 -0.06284,0.1835545 -0.04637,0.046372 -0.112322,0.06284 -0.183554,0.06284 h -0.400183 c -0.07123,0 -0.137183,-0.016468 -0.183555,-0.06284 -0.04637,-0.046369 -0.06284,-0.1123216 -0.06284,-0.1835545 v -0.6206659 h -0.06614 v 0.9254885 c 0,0.07123 -0.01812,0.1355287 -0.06449,0.1819007 -0.04637,0.046372 -0.110668,0.064493 -0.181901,0.064493 h -0.439318 c -0.07123,0 -0.13718,-0.018121 -0.183555,-0.064493 -0.04637,-0.046369 -0.06229,-0.1106678 -0.06229,-0.1819007 v -1.7423919 z m 0,4.0453702 c 0,-0.3375321 0.06795,-0.5988275 0.216625,-0.7755607 0.148548,-0.1737727 0.376205,-0.257968 0.660358,-0.257968 h 1.169678 c 0.28415,0 0.51181,0.084195 0.660355,0.257968 0.148681,0.1767332 0.216628,0.4380286 0.216628,0.7755607 v 1.1812551 c 0,0.071222 -0.01812,0.1371798 -0.06449,0.1835545 -0.04637,0.046369 -0.110118,0.062837 -0.181351,0.062837 h -1.160308 c -0.07123,0 -0.13718,-0.016468 -0.183555,-0.062837 C 17.36839,2.9442533 17.35192,2.8782981 17.35192,2.8070708 V 2.2249875 c 0,-0.07123 0.01647,-0.1371825 0.06284,-0.1835573 0.04637,-0.046369 0.112322,-0.062286 0.183555,-0.062286 h 0.474596 V 1.7272383 c 0,-0.034668 -0.0073,-0.045991 -0.01158,-0.05071 -0.0081,-0.0052 -0.02403,-0.011577 -0.06063,-0.011577 h -0.896826 c -0.03738,0 -0.04506,0.00651 -0.05237,0.017088 l -0.0022,0.0022 c -0.01116,0.014501 -0.02315,0.047021 -0.02315,0.099771 v 0.7788655 c 0,0.07123 -0.01647,0.1371797 -0.06284,0.1835545 -0.04637,0.046369 -0.112322,0.06284 -0.183555,0.06284 h -0.453099 c -0.07123,0 -0.13718,-0.01647 -0.183555,-0.06284 -0.04637,-0.046369 -0.06229,-0.1123216 -0.06229,-0.1835545 V 1.6258106 Z m 0,1.9121655 c 0,-0.07123 0.01592,-0.1355288 0.06229,-0.1819007 0.04637,-0.046372 0.112322,-0.062289 0.183555,-0.062289 h 2.431962 c 0.07123,0 0.134976,0.015917 0.181351,0.062289 0.04637,0.046369 0.06449,0.1106678 0.06449,0.1819007 v 1.7418387 c 0,0.07123 -0.01812,0.1371826 -0.06449,0.1835545 -0.04637,0.046372 -0.110118,0.06284 -0.181351,0.06284 h -0.439871 c -0.07123,0 -0.13718,-0.016468 -0.183555,-0.06284 -0.04637,-0.046369 -0.06229,-0.1123216 -0.06229,-0.1835545 V 4.3543315 h -0.101422 v 0.6206687 c 0,0.07123 -0.01647,0.1371797 -0.06284,0.1835545 -0.04637,0.046369 -0.112322,0.062837 -0.183554,0.062837 h -0.400183 c -0.07123,0 -0.137183,-0.016468 -0.183555,-0.062837 -0.04637,-0.046372 -0.06284,-0.1123216 -0.06284,-0.1835545 V 4.3543315 h -0.06614 v 0.9254884 c 0,0.07123 -0.01812,0.1371826 -0.06449,0.1835545 -0.04637,0.046372 -0.110668,0.06284 -0.181901,0.06284 h -0.439318 c -0.07123,0 -0.13718,-0.016468 -0.183555,-0.06284 -0.04637,-0.046369 -0.06229,-0.1123216 -0.06229,-0.1835545 V 3.5379812 Z m 0,2.4545598 c 0,-0.07123 0.01592,-0.1371797 0.06229,-0.1835545 0.04637,-0.046369 0.112322,-0.062286 0.183555,-0.062286 h 2.431962 c 0.07123,0 0.134976,0.015917 0.181351,0.062286 0.04637,0.046372 0.06449,0.1123216 0.06449,0.1835545 v 0.5627906 c 0,0.07123 -0.01812,0.1371826 -0.06449,0.1835573 -0.04637,0.046369 -0.110118,0.062286 -0.181351,0.062286 h -0.932106 l 0.512081,0.4200256 h 0.420025 c 0.07123,0 0.134976,0.016468 0.181351,0.06284 0.04637,0.046369 0.06449,0.1123216 0.06449,0.1835545 v 0.5622374 c 0,0.07123 -0.01812,0.1371882 -0.06449,0.1835545 -0.04637,0.046375 -0.110118,0.06284 -0.181351,0.06284 h -2.431962 c -0.07123,0 -0.13718,-0.016465 -0.183555,-0.06284 C 16.09674,8.1670239 16.08082,8.1010653 16.08082,8.0298324 V 7.467595 c 0,-0.07123 0.01592,-0.1371826 0.06229,-0.1835545 0.04637,-0.046372 0.112322,-0.06284 0.183555,-0.06284 h 0.4983 L 16.217524,6.6898297 v -0.00165 c -0.04502,-0.04222 -0.08102,-0.086067 -0.103629,-0.1344958 -0.02332,-0.04997 -0.03307,-0.1075238 -0.03307,-0.1703267 V 5.9930975 5.9925443 Z m 0,2.6761521 c 0,-0.07123 0.01592,-0.137182 0.06229,-0.183554 0.04637,-0.046372 0.112322,-0.06284 0.183555,-0.06284 h 0.453099 c 0.07123,0 0.137183,0.016468 0.183555,0.06284 0.04637,0.04637 0.06284,0.112321 0.06284,0.183554 v 0.439319 h 1.732469 c 0.07123,0 0.134976,0.01592 0.181351,0.06229 0.04637,0.04637 0.06449,0.112872 0.06449,0.184105 v 0.606888 c 0,0.07123 -0.01812,0.1377329 -0.06449,0.1841069 -0.04637,0.04637 -0.110118,0.06229 -0.181351,0.06229 h -1.732469 v 0.441522 c 0,0.07123 -0.01647,0.13718 -0.06284,0.183558 -0.04637,0.04637 -0.112322,0.06229 -0.183555,0.06229 h -0.453099 c -0.07123,0 -0.13718,-0.01592 -0.183555,-0.06229 -0.04637,-0.04637 -0.06229,-0.112325 -0.06229,-0.183558 V 8.6687001 Z M 16.264374,-7.884302 v 1.9805169 c 0,0.035941 0.0089,0.046002 0.0099,0.046855 l 0.0055,0.00606 c 8.53e-4,9.51e-4 0.01093,0.00992 0.04686,0.00992 h 0.453099 c 0.03594,0 0.05082,-0.00951 0.05512,-0.013781 -5e-4,5.249e-4 0.0077,-0.011828 0.0077,-0.049059 v -0.5506635 c -4.91e-4,-0.04119 0.03267,-0.074893 0.07386,-0.074414 h 1.842163 c 0.03594,0 0.04807,-0.00736 0.05236,-0.011577 -5e-4,5.278e-4 0.0083,-0.01349 0.0083,-0.050712 v -0.6074381 c 0,-0.032049 -0.0062,-0.042511 -0.0099,-0.048506 -0.0047,-0.0034 -0.01603,-0.012127 -0.05071,-0.012127 h -1.842163 c -0.04119,4.826e-4 -0.07434,-0.032673 -0.07386,-0.073863 v -0.5512167 c -3e-6,-0.03451 -0.0064,-0.047546 -0.0099,-0.052364 -0.0048,-0.0034 -0.01842,-0.00992 -0.05292,-0.00992 h -0.453099 c -0.03721,0 -0.04903,0.010411 -0.04851,0.00992 -0.0043,0.0043 -0.01378,0.016434 -0.01378,0.052364 z m 0,2.6155168 v 0.5820833 c 0,0.035941 0.0089,0.046013 0.0099,0.046855 l 0.0055,0.00551 c 8.53e-4,9.595e-4 0.01093,0.00827 0.04686,0.00827 h 0.814696 c 0.04042,6.096e-4 0.07269,0.033441 0.07221,0.073863 v 0.627284 c -5.9e-4,0.039664 -0.03255,0.071617 -0.07221,0.072209 h -0.814696 c -0.03721,0 -0.04903,0.010408 -0.04851,0.00992 -0.0043,0.00429 -0.01378,0.016434 -0.01378,0.052363 v 0.5820833 c 0,0.035941 0.0089,0.044351 0.0099,0.045201 0.0021,0.00247 0.0037,0.00499 0.0055,0.00772 8.53e-4,9.596e-4 0.01093,0.00772 0.04686,0.00772 h 2.431962 c 0.03594,0 0.04862,-0.00736 0.05292,-0.011577 -4.99e-4,5.362e-4 0.0077,-0.011828 0.0077,-0.049059 v -0.5820833 c 0,-0.03451 -0.0064,-0.048096 -0.0099,-0.052917 -0.0049,-0.0034 -0.0163,-0.00937 -0.05071,-0.00937 h -0.833989 c -0.03966,-5.87e-4 -0.07162,-0.032546 -0.07221,-0.072209 v -0.627284 c -4.8e-4,-0.040426 0.03178,-0.073262 0.07221,-0.073863 h 0.833989 c 0.03594,0 0.04807,-0.00791 0.05236,-0.012124 -5e-4,5.334e-4 0.0083,-0.011289 0.0083,-0.048508 v -0.5820833 c 0,-0.03451 -0.0064,-0.048096 -0.0099,-0.052917 -0.0049,-0.0035 -0.0163,-0.00992 -0.05071,-0.00992 h -2.431962 c -0.03721,0 -0.04903,0.010414 -0.04851,0.00992 -0.0043,0.0043 -0.01378,0.016987 -0.01378,0.052917 z m 0,2.8492307 v 1.7423919 c 0,0.035941 0.0089,0.044351 0.0099,0.045201 0.0021,0.00247 0.0037,0.00499 0.0055,0.00772 8.53e-4,9.595e-4 0.01093,0.00772 0.04686,0.00772 h 0.439869 c 0.03594,0 0.04807,-0.00736 0.05237,-0.011577 -5e-4,5.362e-4 0.0077,-0.011839 0.0077,-0.049059 v -1.0351826 c -4.8e-4,-0.041187 0.03323,-0.074896 0.07442,-0.074413 h 0.288835 c 0.04043,6.012e-4 0.07324,0.033988 0.07276,0.074413 v 0.73036 c 0,0.035941 0.0084,0.046014 0.0094,0.046855 l 0.0061,0.00606 c 8.53e-4,9.624e-4 0.01091,0.00992 0.04686,0.00992 h 0.400183 c 0.03594,0 0.05082,-0.00951 0.05512,-0.013781 -4.99e-4,5.363e-4 0.0077,-0.011836 0.0077,-0.049059 v -0.73036 c -4.88e-4,-0.041187 0.03267,-0.074346 0.07386,-0.073863 h 0.322461 c 0.04043,6.012e-4 0.07269,0.033438 0.07221,0.073863 v 1.0351826 c 0,0.035941 0.0089,0.044351 0.0099,0.045201 0.0021,0.00247 0.0043,0.00499 0.0061,0.00772 8.5e-4,9.595e-4 0.01093,0.00772 0.04686,0.00772 h 0.439318 c 0.03594,0 0.04862,-0.00736 0.05292,-0.011577 -4.99e-4,5.362e-4 0.0077,-0.011839 0.0077,-0.049059 v -1.7423919 c 0,-0.034408 -0.0064,-0.04583 -0.0099,-0.05071 -0.0049,-0.0034 -0.0163,-0.00937 -0.05071,-0.00937 h -2.431962 c -0.03721,0 -0.04903,0.00822 -0.04851,0.00772 -0.0043,0.0043 -0.01378,0.016434 -0.01378,0.052364 z m 0,4.0453702 v 0.9370652 c 0,0.035941 0.0089,0.046013 0.0099,0.046855 l 0.0055,0.00606 c 8.53e-4,9.595e-4 0.01093,0.00992 0.04686,0.00992 h 0.453099 c 0.03594,0 0.05082,-0.00951 0.05512,-0.013781 -5e-4,5.362e-4 0.0077,-0.011278 0.0077,-0.048508 V 1.7840111 c -3e-6,-0.087074 0.01814,-0.1625516 0.06614,-0.2188351 0.04561,-0.055937 0.119132,-0.083783 0.195682,-0.083783 h 0.896275 c 0.07329,0 0.138693,0.015423 0.187413,0.060082 l 0.0022,0.0022 c 0.04658,0.046581 0.06614,0.1132727 0.06614,0.1835545 v 0.363251 c 4.8e-4,0.040428 -0.03178,0.073815 -0.07221,0.074414 h -0.585941 c -0.03722,0 -0.04903,0.00822 -0.04851,0.00772 -0.0043,0.0043 -0.01212,0.016434 -0.01212,0.052366 v 0.5820833 c 0,0.035933 0.0068,0.046011 0.0077,0.046852 l 0.0061,0.00607 c 8.41e-4,9.567e-4 0.01093,0.00992 0.04686,0.00992 h 1.160308 c 0.03594,0 0.04862,-0.00951 0.05292,-0.013781 -4.99e-4,5.362e-4 0.0077,-0.011831 0.0077,-0.049056 V 1.6258137 c 0,-0.3020003 -0.06142,-0.5167884 -0.170324,-0.6504347 C 18.539841,0.844538 18.373437,0.7758395 18.127435,0.7758395 h -1.169678 c -0.246002,0 -0.412411,0.06869 -0.521451,0.1995395 -0.108907,0.1336463 -0.171978,0.3484315 -0.171978,0.6504347 z m 0,1.9121655 v 1.7418387 c 0,0.035941 0.0089,0.046013 0.0099,0.046855 l 0.0055,0.00606 c 8.53e-4,9.623e-4 0.01093,0.00772 0.04686,0.00772 h 0.439869 c 0.03594,0 0.04807,-0.00736 0.05237,-0.011577 -5e-4,5.362e-4 0.0077,-0.011828 0.0077,-0.049059 V 4.2446363 c -4.8e-4,-0.041182 0.03323,-0.074346 0.07442,-0.07386 h 0.288835 c 0.04043,5.983e-4 0.07324,0.033438 0.07276,0.07386 v 0.7303629 c 0,0.035938 0.0084,0.046011 0.0094,0.046852 l 0.0061,0.00606 c 8.53e-4,9.596e-4 0.01091,0.00992 0.04686,0.00992 h 0.400183 c 0.03594,0 0.05082,-0.00951 0.05512,-0.013781 -4.99e-4,5.363e-4 0.0077,-0.011275 0.0077,-0.048506 V 4.244631 c -4.88e-4,-0.041182 0.03267,-0.074346 0.07386,-0.07386 h 0.322461 c 0.04043,5.983e-4 0.07269,0.033438 0.07221,0.07386 v 1.0351826 c 0,0.035941 0.0089,0.046005 0.0099,0.046855 l 0.0061,0.00606 c 8.5e-4,9.623e-4 0.01093,0.00772 0.04686,0.00772 h 0.439318 c 0.03594,0 0.04862,-0.00736 0.05292,-0.011577 -4.99e-4,5.362e-4 0.0077,-0.011828 0.0077,-0.049059 V 3.5379739 c 0,-0.034411 -0.0064,-0.045833 -0.0099,-0.050713 -0.0049,-0.0034 -0.0163,-0.00992 -0.05071,-0.00992 h -2.431962 c -0.03721,0 -0.04903,0.00822 -0.04851,0.00772 -0.0043,0.0043 -0.01378,0.016987 -0.01378,0.052917 z m 0,2.4545598 v 0.3908129 c 0,0.039799 0.0061,0.069689 0.01543,0.089848 l 0.0022,0.0022 c 0.0095,0.022231 0.02711,0.046713 0.05843,0.073863 l 0.833989,0.7287062 c 0.05182,0.04471 0.01938,0.1298306 -0.04906,0.128984 h -0.798711 c -0.03721,0 -0.04903,0.00822 -0.04851,0.00772 -0.0043,0.0043 -0.01378,0.016987 -0.01378,0.052917 v 0.5622374 c 0,0.035941 0.0084,0.046013 0.0094,0.046855 l 0.0061,0.00606 c 8.53e-4,9.624e-4 0.01093,0.00992 0.04686,0.00992 h 2.431962 c 0.03594,0 0.04807,-0.00791 0.05236,-0.012127 -5e-4,5.363e-4 0.0077,-0.01349 0.0077,-0.050712 V 7.4675881 c 0,-0.03328 -0.0058,-0.045282 -0.0094,-0.050712 -0.0048,-0.0034 -0.01606,-0.00992 -0.05071,-0.00992 h -0.463022 c -0.0172,-1.835e-4 -0.03377,-0.00647 -0.04685,-0.017639 l -0.77556,-0.6427159 c -0.05109,-0.044078 -0.02062,-0.1280188 0.04685,-0.128984 h 1.23858 c 0.03594,0 0.04807,-0.00735 0.05236,-0.011577 -5e-4,5.39e-4 0.0077,-0.01349 0.0077,-0.050712 V 5.9925376 c 0,-0.032049 -0.0057,-0.042506 -0.0094,-0.048506 -0.0047,-0.0034 -0.01603,-0.011577 -0.05071,-0.011577 H 16.32662 c -0.03721,0 -0.04903,0.00822 -0.04851,0.00772 -0.0043,0.0043 -0.01378,0.016434 -0.01378,0.052364 z m 0,2.6761521 v 1.9805139 c 0,0.03595 0.0089,0.04601 0.0099,0.04686 l 0.0055,0.0055 c 8.53e-4,9.99e-4 0.01093,0.0083 0.04686,0.0083 h 0.453099 c 0.03594,0 0.05082,-0.0079 0.05512,-0.01213 -5e-4,5.39e-4 0.0077,-0.01128 0.0077,-0.04851 V 10.09636 c 5.95e-4,-0.04043 0.03343,-0.07269 0.07386,-0.07221 h 1.842163 c 0.03594,0 0.04807,-0.0074 0.05236,-0.01158 -5e-4,5.42e-4 0.0083,-0.01349 0.0083,-0.05071 v -0.607441 c 0,-0.03328 -0.0063,-0.04586 -0.0099,-0.05126 -0.0047,-0.0034 -0.01607,-0.0094 -0.05071,-0.0094 h -1.842163 c -0.04119,4.91e-4 -0.07434,-0.03322 -0.07386,-0.07441 v -0.550664 c -3e-6,-0.03451 -0.0064,-0.04812 -0.0099,-0.05292 -0.0048,-0.0034 -0.01842,-0.0099 -0.05292,-0.0099 h -0.453099 c -0.03721,0 -0.04903,0.0082 -0.04851,0.0077 -0.0043,0.0043 -0.01378,0.01918 -0.01378,0.05512 z m 0.187413,-2.3713295 c 0,-0.028338 0.01081,-0.054472 0.02536,-0.073863 0.02159,-0.028778 0.0624,-0.045198 0.09371,-0.045198 h 1.984375 c 0.04043,5.983e-4 0.07269,0.033985 0.07221,0.074413 v 0.036932 c 4.77e-4,0.040426 -0.03178,0.073812 -0.07221,0.074414 h -1.812394 l 1.453004,1.2964583 h 0.35939 c 0.04043,6.011e-4 0.07269,0.033988 0.07221,0.074414 v 0.036932 c -5.87e-4,0.039669 -0.03254,0.072173 -0.07221,0.07276 h -2.025165 c -0.04043,4.77e-4 -0.07381,-0.032334 -0.07441,-0.07276 v -0.036932 c -4.83e-4,-0.041187 0.03322,-0.074896 0.07441,-0.074414 h 1.388514 l -1.408357,-1.2518107 -0.0039,-0.00386 c -0.01423,-0.01423 -0.02506,-0.025459 -0.03528,-0.04079 -0.01335,-0.020021 -0.01929,-0.044467 -0.01929,-0.066698 z m 0.0039,-13.985984 c 0.0036,-0.038108 0.03614,-0.067316 0.07441,-0.066698 h 0.03693 c 0.04043,6.012e-4 0.07269,0.033985 0.07221,0.074416 v 0.6950822 h 1.916024 c 0.03967,5.87e-4 0.07162,0.032537 0.07221,0.072209 v 0.037482 c 4.77e-4,0.040428 -0.03178,0.073262 -0.07221,0.073863 h -1.916024 v 0.6956326 c 4.77e-4,0.040431 -0.03178,0.073262 -0.07221,0.073863 h -0.03693 c -0.04119,4.826e-4 -0.07489,-0.032673 -0.07441,-0.073863 v -1.5742693 -0.00772 z m 0,2.6833151 c 0.0036,-0.038106 0.03614,-0.066762 0.07441,-0.066145 h 2.025165 c 0.03967,5.871e-4 0.07162,0.03254 0.07221,0.072209 v 0.039136 c -5.87e-4,0.039669 -0.03254,0.071622 -0.07221,0.072209 h -0.921631 v 1.2948045 h 0.921631 c 0.03966,5.87e-4 0.07162,0.032546 0.07221,0.072209 v 0.036932 c 4.77e-4,0.040426 -0.03178,0.073815 -0.07221,0.074413 h -2.025165 c -0.04119,4.855e-4 -0.07489,-0.033226 -0.07441,-0.074413 v -0.036932 c 6.04e-4,-0.040423 0.03399,-0.072686 0.07441,-0.072209 h 0.91998 v -1.2948045 h -0.91998 c -0.04043,4.77e-4 -0.07381,-0.031784 -0.07441,-0.072209 v -0.039136 -0.00606 z m 0,2.8536418 c 0.0036,-0.038111 0.03614,-0.067316 0.07441,-0.066698 h 2.025165 c 0.04043,6.011e-4 0.07269,0.033988 0.07221,0.074416 v 1.2639349 c 4.77e-4,0.040428 -0.03178,0.073262 -0.07221,0.073863 h -0.03693 c -0.04119,4.826e-4 -0.0749,-0.032673 -0.07442,-0.073863 v -1.1547968 h -0.824066 v 0.8499742 c 4.85e-4,0.04119 -0.03322,0.074349 -0.07441,0.073863 h -0.03693 c -0.04119,4.855e-4 -0.07489,-0.032673 -0.07441,-0.073863 v -0.8499742 h -0.794854 v 1.1547968 c 4.77e-4,0.040428 -0.03178,0.073262 -0.07221,0.073863 h -0.03693 c -0.04119,4.826e-4 -0.07489,-0.032673 -0.07441,-0.073863 v -1.2639349 -0.00772 z m 0,3.8629163 c 5.4e-5,-0.2474298 0.03286,-0.4225148 0.132842,-0.5291666 0.09478,-0.1010976 0.243007,-0.1444159 0.431602,-0.1444187 h 1.050618 c 0.09243,0 0.173101,0.00932 0.244187,0.029216 l 0.0039,0.0022 c 0.07278,0.02426 0.137546,0.068718 0.185761,0.128984 0.04655,0.062072 0.07696,0.1411393 0.09591,0.2359208 0.01896,0.094781 0.02701,0.2110062 0.02701,0.3516743 v 0.7479988 c -5.87e-4,0.039666 -0.03255,0.071622 -0.07221,0.072209 h -0.754061 c -0.04042,4.77e-4 -0.07326,-0.031787 -0.07386,-0.072209 v -0.036929 c -4.83e-4,-0.04119 0.03267,-0.074899 0.07386,-0.074416 h 0.642716 V 1.7856627 c 0,-0.2450677 -0.03955,-0.401955 -0.08599,-0.4630194 -0.0497,-0.062591 -0.137405,-0.099218 -0.287183,-0.099218 h -1.050618 c -0.153582,0 -0.24461,0.034637 -0.292695,0.089848 v 0.00165 c -0.04689,0.051918 -0.08819,0.1840117 -0.08819,0.3963218 V 2.360026 c 4.77e-4,0.040426 -0.03179,0.073259 -0.07221,0.073863 h -0.03693 c -0.04119,4.826e-4 -0.07489,-0.032673 -0.07441,-0.073863 V 1.7117983 1.7112451 Z m 0,2.0940662 c 0.0036,-0.038106 0.03614,-0.066763 0.07441,-0.066144 h 2.025165 c 0.04043,5.983e-4 0.07269,0.033435 0.07221,0.073863 v 1.263935 c 4.77e-4,0.040428 -0.03178,0.073265 -0.07221,0.073863 h -0.03693 c -0.04119,4.854e-4 -0.0749,-0.032673 -0.07442,-0.073863 V 3.9227294 h -0.824066 v 0.8494239 c 4.85e-4,0.041188 -0.03322,0.074896 -0.07441,0.074414 h -0.03693 c -0.04119,4.826e-4 -0.07489,-0.033226 -0.07441,-0.074414 V 3.9227294 H 16.639242 V 5.076973 c 4.77e-4,0.040428 -0.03178,0.073265 -0.07221,0.073863 h -0.03693 c -0.04119,4.854e-4 -0.07489,-0.032673 -0.07441,-0.073863 V 3.813038 3.805318 Z m 0,5.0585031 c 0.0036,-0.03811 0.03614,-0.06677 0.07441,-0.06614 h 0.03693 c 0.03967,5.87e-4 0.07162,0.03254 0.07221,0.07221 v 0.697286 h 1.916024 c 0.03967,5.87e-4 0.07162,0.03254 0.07221,0.07221 v 0.03693 c 4.77e-4,0.04043 -0.03178,0.07381 -0.07221,0.07441 h -1.916024 v 0.6950829 c 4.77e-4,0.04043 -0.03178,0.07381 -0.07221,0.07441 h -0.03693 c -0.04119,4.88e-4 -0.07489,-0.03322 -0.07441,-0.07441 v -1.5759229 -0.0061 z",
        ]

        for path in svg_paths:
            with self.subTest(path=path):
                result = grammar.parseString(path)
