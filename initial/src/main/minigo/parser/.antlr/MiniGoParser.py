# Generated from c://Users//HP//Downloads//Principles of Programming Language (CO3005)//Assignment//Assignment 2//initial//initial//src//main//minigo//parser//MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,65,590,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,1,0,4,0,126,8,0,11,0,12,0,127,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,138,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,150,8,2,1,3,1,3,4,3,154,8,3,11,3,12,3,155,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,169,8,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,187,8,7,1,8,
        1,8,1,8,3,8,192,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,5,
        10,204,8,10,10,10,12,10,207,9,10,1,11,1,11,1,11,1,12,1,12,1,12,3,
        12,215,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,3,15,241,8,15,1,15,1,15,3,15,245,8,15,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,19,
        1,19,1,19,1,20,1,20,3,20,269,8,20,1,20,1,20,1,21,1,21,3,21,275,8,
        21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,283,8,22,1,22,1,22,3,22,287,
        8,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,295,8,23,1,23,1,23,1,24,
        1,24,1,24,5,24,302,8,24,10,24,12,24,305,9,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,3,25,315,8,25,1,25,1,25,3,25,319,8,25,1,25,1,
        25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,3,28,333,8,
        28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,341,8,29,10,29,12,29,344,9,
        29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,352,8,30,10,30,12,30,355,9,
        30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,364,8,31,10,31,12,31,
        367,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,5,32,376,8,32,10,32,
        12,32,379,9,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,388,8,33,
        10,33,12,33,391,9,33,1,34,1,34,1,34,3,34,396,8,34,1,35,1,35,1,35,
        1,35,3,35,402,8,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,3,37,418,8,37,1,38,1,38,1,38,1,38,1,38,
        1,38,3,38,426,8,38,3,38,428,8,38,1,39,1,39,1,39,1,39,1,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,41,1,41,1,42,1,42,1,42,5,42,446,8,42,10,
        42,12,42,449,9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,459,
        8,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,3,45,470,8,45,
        1,45,4,45,473,8,45,11,45,12,45,474,1,45,1,45,4,45,479,8,45,11,45,
        12,45,480,3,45,483,8,45,1,46,1,46,1,46,1,46,1,46,4,46,490,8,46,11,
        46,12,46,491,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,3,
        48,504,8,48,1,48,1,48,1,49,1,49,1,49,5,49,511,8,49,10,49,12,49,514,
        9,49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,
        4,52,528,8,52,11,52,12,52,529,1,52,1,52,5,52,534,8,52,10,52,12,52,
        537,9,52,1,53,1,53,1,53,1,53,1,53,4,53,544,8,53,11,53,12,53,545,
        1,53,1,53,1,53,1,54,1,54,1,54,3,54,554,8,54,1,54,1,54,3,54,558,8,
        54,1,54,1,54,1,55,1,55,1,55,5,55,565,8,55,10,55,12,55,568,9,55,1,
        56,1,56,1,56,5,56,573,8,56,10,56,12,56,576,9,56,1,56,1,56,1,57,1,
        57,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,1,61,0,5,58,60,62,64,
        66,62,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,
        122,0,8,1,0,11,14,2,0,21,21,33,33,2,0,51,51,62,62,1,0,22,24,1,0,
        20,21,1,0,25,30,1,0,34,39,1,0,1,2,607,0,125,1,0,0,0,2,137,1,0,0,
        0,4,149,1,0,0,0,6,151,1,0,0,0,8,159,1,0,0,0,10,172,1,0,0,0,12,178,
        1,0,0,0,14,186,1,0,0,0,16,188,1,0,0,0,18,195,1,0,0,0,20,205,1,0,
        0,0,22,208,1,0,0,0,24,214,1,0,0,0,26,216,1,0,0,0,28,221,1,0,0,0,
        30,244,1,0,0,0,32,246,1,0,0,0,34,250,1,0,0,0,36,260,1,0,0,0,38,263,
        1,0,0,0,40,268,1,0,0,0,42,272,1,0,0,0,44,278,1,0,0,0,46,291,1,0,
        0,0,48,298,1,0,0,0,50,306,1,0,0,0,52,323,1,0,0,0,54,327,1,0,0,0,
        56,332,1,0,0,0,58,334,1,0,0,0,60,345,1,0,0,0,62,356,1,0,0,0,64,368,
        1,0,0,0,66,380,1,0,0,0,68,395,1,0,0,0,70,401,1,0,0,0,72,403,1,0,
        0,0,74,417,1,0,0,0,76,427,1,0,0,0,78,429,1,0,0,0,80,433,1,0,0,0,
        82,437,1,0,0,0,84,442,1,0,0,0,86,458,1,0,0,0,88,460,1,0,0,0,90,482,
        1,0,0,0,92,484,1,0,0,0,94,496,1,0,0,0,96,500,1,0,0,0,98,507,1,0,
        0,0,100,515,1,0,0,0,102,519,1,0,0,0,104,523,1,0,0,0,106,538,1,0,
        0,0,108,550,1,0,0,0,110,561,1,0,0,0,112,569,1,0,0,0,114,579,1,0,
        0,0,116,581,1,0,0,0,118,583,1,0,0,0,120,585,1,0,0,0,122,587,1,0,
        0,0,124,126,3,2,1,0,125,124,1,0,0,0,126,127,1,0,0,0,127,125,1,0,
        0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,130,5,0,0,1,130,1,1,0,0,
        0,131,138,3,8,4,0,132,138,3,10,5,0,133,138,3,92,46,0,134,138,3,106,
        53,0,135,138,3,44,22,0,136,138,3,50,25,0,137,131,1,0,0,0,137,132,
        1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,0,0,0,137,136,
        1,0,0,0,138,3,1,0,0,0,139,150,3,8,4,0,140,150,3,10,5,0,141,150,3,
        12,6,0,142,150,3,16,8,0,143,150,3,24,12,0,144,150,3,36,18,0,145,
        150,3,38,19,0,146,150,3,40,20,0,147,150,3,42,21,0,148,150,3,122,
        61,0,149,139,1,0,0,0,149,140,1,0,0,0,149,141,1,0,0,0,149,142,1,0,
        0,0,149,143,1,0,0,0,149,144,1,0,0,0,149,145,1,0,0,0,149,146,1,0,
        0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,5,1,0,0,0,151,153,5,46,0,
        0,152,154,3,4,2,0,153,152,1,0,0,0,154,155,1,0,0,0,155,153,1,0,0,
        0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,47,0,0,158,7,1,0,0,0,
        159,160,5,16,0,0,160,168,5,62,0,0,161,169,3,56,28,0,162,163,5,40,
        0,0,163,169,3,58,29,0,164,165,3,56,28,0,165,166,5,40,0,0,166,167,
        3,58,29,0,167,169,1,0,0,0,168,161,1,0,0,0,168,162,1,0,0,0,168,164,
        1,0,0,0,169,170,1,0,0,0,170,171,5,49,0,0,171,9,1,0,0,0,172,173,5,
        15,0,0,173,174,5,62,0,0,174,175,5,40,0,0,175,176,3,58,29,0,176,177,
        5,49,0,0,177,11,1,0,0,0,178,179,3,14,7,0,179,180,3,120,60,0,180,
        181,3,58,29,0,181,182,5,49,0,0,182,13,1,0,0,0,183,187,5,62,0,0,184,
        187,3,102,51,0,185,187,3,90,45,0,186,183,1,0,0,0,186,184,1,0,0,0,
        186,185,1,0,0,0,187,15,1,0,0,0,188,189,3,18,9,0,189,191,3,20,10,
        0,190,192,3,22,11,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,
        0,0,193,194,5,49,0,0,194,17,1,0,0,0,195,196,5,3,0,0,196,197,5,42,
        0,0,197,198,3,58,29,0,198,199,5,43,0,0,199,200,3,6,3,0,200,19,1,
        0,0,0,201,202,5,4,0,0,202,204,3,18,9,0,203,201,1,0,0,0,204,207,1,
        0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,21,1,0,0,0,207,205,1,0,
        0,0,208,209,5,4,0,0,209,210,3,6,3,0,210,23,1,0,0,0,211,215,3,26,
        13,0,212,215,3,28,14,0,213,215,3,34,17,0,214,211,1,0,0,0,214,212,
        1,0,0,0,214,213,1,0,0,0,215,25,1,0,0,0,216,217,5,5,0,0,217,218,3,
        58,29,0,218,219,3,6,3,0,219,220,5,49,0,0,220,27,1,0,0,0,221,222,
        5,5,0,0,222,223,3,30,15,0,223,224,3,58,29,0,224,225,5,49,0,0,225,
        226,3,32,16,0,226,227,3,6,3,0,227,228,5,49,0,0,228,29,1,0,0,0,229,
        230,3,32,16,0,230,231,5,49,0,0,231,245,1,0,0,0,232,233,5,16,0,0,
        233,240,5,62,0,0,234,235,5,40,0,0,235,241,3,58,29,0,236,237,3,56,
        28,0,237,238,5,40,0,0,238,239,3,58,29,0,239,241,1,0,0,0,240,234,
        1,0,0,0,240,236,1,0,0,0,241,242,1,0,0,0,242,243,5,49,0,0,243,245,
        1,0,0,0,244,229,1,0,0,0,244,232,1,0,0,0,245,31,1,0,0,0,246,247,5,
        62,0,0,247,248,3,120,60,0,248,249,3,58,29,0,249,33,1,0,0,0,250,251,
        5,5,0,0,251,252,5,62,0,0,252,253,5,48,0,0,253,254,5,62,0,0,254,255,
        5,34,0,0,255,256,5,19,0,0,256,257,3,58,29,0,257,258,3,6,3,0,258,
        259,5,49,0,0,259,35,1,0,0,0,260,261,5,18,0,0,261,262,5,49,0,0,262,
        37,1,0,0,0,263,264,5,17,0,0,264,265,5,49,0,0,265,39,1,0,0,0,266,
        269,3,46,23,0,267,269,3,52,26,0,268,266,1,0,0,0,268,267,1,0,0,0,
        269,270,1,0,0,0,270,271,5,49,0,0,271,41,1,0,0,0,272,274,5,6,0,0,
        273,275,3,58,29,0,274,273,1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,
        0,276,277,5,49,0,0,277,43,1,0,0,0,278,279,5,7,0,0,279,280,5,62,0,
        0,280,282,5,42,0,0,281,283,3,110,55,0,282,281,1,0,0,0,282,283,1,
        0,0,0,283,284,1,0,0,0,284,286,5,43,0,0,285,287,3,56,28,0,286,285,
        1,0,0,0,286,287,1,0,0,0,287,288,1,0,0,0,288,289,3,6,3,0,289,290,
        5,49,0,0,290,45,1,0,0,0,291,292,5,62,0,0,292,294,5,42,0,0,293,295,
        3,48,24,0,294,293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,297,
        5,43,0,0,297,47,1,0,0,0,298,303,3,58,29,0,299,300,5,48,0,0,300,302,
        3,58,29,0,301,299,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,49,1,0,0,0,305,303,1,0,0,0,306,307,5,7,0,0,307,308,5,
        42,0,0,308,309,5,62,0,0,309,310,5,62,0,0,310,311,5,43,0,0,311,312,
        5,62,0,0,312,314,5,42,0,0,313,315,3,110,55,0,314,313,1,0,0,0,314,
        315,1,0,0,0,315,316,1,0,0,0,316,318,5,43,0,0,317,319,3,56,28,0,318,
        317,1,0,0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,321,3,6,3,0,321,
        322,5,49,0,0,322,51,1,0,0,0,323,324,3,104,52,0,324,325,5,41,0,0,
        325,326,3,46,23,0,326,53,1,0,0,0,327,328,7,0,0,0,328,55,1,0,0,0,
        329,333,3,54,27,0,330,333,5,62,0,0,331,333,3,76,38,0,332,329,1,0,
        0,0,332,330,1,0,0,0,332,331,1,0,0,0,333,57,1,0,0,0,334,335,6,29,
        -1,0,335,336,3,60,30,0,336,342,1,0,0,0,337,338,10,2,0,0,338,339,
        5,32,0,0,339,341,3,60,30,0,340,337,1,0,0,0,341,344,1,0,0,0,342,340,
        1,0,0,0,342,343,1,0,0,0,343,59,1,0,0,0,344,342,1,0,0,0,345,346,6,
        30,-1,0,346,347,3,62,31,0,347,353,1,0,0,0,348,349,10,2,0,0,349,350,
        5,31,0,0,350,352,3,62,31,0,351,348,1,0,0,0,352,355,1,0,0,0,353,351,
        1,0,0,0,353,354,1,0,0,0,354,61,1,0,0,0,355,353,1,0,0,0,356,357,6,
        31,-1,0,357,358,3,64,32,0,358,365,1,0,0,0,359,360,10,2,0,0,360,361,
        3,118,59,0,361,362,3,64,32,0,362,364,1,0,0,0,363,359,1,0,0,0,364,
        367,1,0,0,0,365,363,1,0,0,0,365,366,1,0,0,0,366,63,1,0,0,0,367,365,
        1,0,0,0,368,369,6,32,-1,0,369,370,3,66,33,0,370,377,1,0,0,0,371,
        372,10,2,0,0,372,373,3,116,58,0,373,374,3,66,33,0,374,376,1,0,0,
        0,375,371,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,
        0,378,65,1,0,0,0,379,377,1,0,0,0,380,381,6,33,-1,0,381,382,3,68,
        34,0,382,389,1,0,0,0,383,384,10,2,0,0,384,385,3,114,57,0,385,386,
        3,68,34,0,386,388,1,0,0,0,387,383,1,0,0,0,388,391,1,0,0,0,389,387,
        1,0,0,0,389,390,1,0,0,0,390,67,1,0,0,0,391,389,1,0,0,0,392,393,7,
        1,0,0,393,396,3,68,34,0,394,396,3,70,35,0,395,392,1,0,0,0,395,394,
        1,0,0,0,396,69,1,0,0,0,397,402,3,102,51,0,398,402,3,90,45,0,399,
        402,3,52,26,0,400,402,3,74,37,0,401,397,1,0,0,0,401,398,1,0,0,0,
        401,399,1,0,0,0,401,400,1,0,0,0,402,71,1,0,0,0,403,404,5,42,0,0,
        404,405,3,58,29,0,405,406,5,43,0,0,406,73,1,0,0,0,407,418,5,51,0,
        0,408,418,5,56,0,0,409,418,5,57,0,0,410,418,5,58,0,0,411,418,5,59,
        0,0,412,418,3,82,41,0,413,418,3,96,48,0,414,418,5,62,0,0,415,418,
        3,46,23,0,416,418,3,72,36,0,417,407,1,0,0,0,417,408,1,0,0,0,417,
        409,1,0,0,0,417,410,1,0,0,0,417,411,1,0,0,0,417,412,1,0,0,0,417,
        413,1,0,0,0,417,414,1,0,0,0,417,415,1,0,0,0,417,416,1,0,0,0,418,
        75,1,0,0,0,419,420,3,78,39,0,420,421,3,76,38,0,421,428,1,0,0,0,422,
        425,3,78,39,0,423,426,3,54,27,0,424,426,5,62,0,0,425,423,1,0,0,0,
        425,424,1,0,0,0,426,428,1,0,0,0,427,419,1,0,0,0,427,422,1,0,0,0,
        428,77,1,0,0,0,429,430,5,44,0,0,430,431,7,2,0,0,431,432,5,45,0,0,
        432,79,1,0,0,0,433,434,5,44,0,0,434,435,3,58,29,0,435,436,5,45,0,
        0,436,81,1,0,0,0,437,438,3,76,38,0,438,439,5,46,0,0,439,440,3,84,
        42,0,440,441,5,47,0,0,441,83,1,0,0,0,442,447,3,86,43,0,443,444,5,
        48,0,0,444,446,3,86,43,0,445,443,1,0,0,0,446,449,1,0,0,0,447,445,
        1,0,0,0,447,448,1,0,0,0,448,85,1,0,0,0,449,447,1,0,0,0,450,459,5,
        51,0,0,451,459,5,56,0,0,452,459,5,58,0,0,453,459,5,57,0,0,454,459,
        5,59,0,0,455,459,5,62,0,0,456,459,3,96,48,0,457,459,3,88,44,0,458,
        450,1,0,0,0,458,451,1,0,0,0,458,452,1,0,0,0,458,453,1,0,0,0,458,
        454,1,0,0,0,458,455,1,0,0,0,458,456,1,0,0,0,458,457,1,0,0,0,459,
        87,1,0,0,0,460,461,5,46,0,0,461,462,3,84,42,0,462,463,5,47,0,0,463,
        89,1,0,0,0,464,469,3,104,52,0,465,466,5,41,0,0,466,470,5,62,0,0,
        467,468,5,41,0,0,468,470,3,46,23,0,469,465,1,0,0,0,469,467,1,0,0,
        0,470,472,1,0,0,0,471,473,3,80,40,0,472,471,1,0,0,0,473,474,1,0,
        0,0,474,472,1,0,0,0,474,475,1,0,0,0,475,483,1,0,0,0,476,478,3,74,
        37,0,477,479,3,80,40,0,478,477,1,0,0,0,479,480,1,0,0,0,480,478,1,
        0,0,0,480,481,1,0,0,0,481,483,1,0,0,0,482,464,1,0,0,0,482,476,1,
        0,0,0,483,91,1,0,0,0,484,485,5,8,0,0,485,486,5,62,0,0,486,487,5,
        9,0,0,487,489,5,46,0,0,488,490,3,94,47,0,489,488,1,0,0,0,490,491,
        1,0,0,0,491,489,1,0,0,0,491,492,1,0,0,0,492,493,1,0,0,0,493,494,
        5,47,0,0,494,495,5,49,0,0,495,93,1,0,0,0,496,497,5,62,0,0,497,498,
        3,56,28,0,498,499,5,49,0,0,499,95,1,0,0,0,500,501,5,62,0,0,501,503,
        5,46,0,0,502,504,3,98,49,0,503,502,1,0,0,0,503,504,1,0,0,0,504,505,
        1,0,0,0,505,506,5,47,0,0,506,97,1,0,0,0,507,512,3,100,50,0,508,509,
        5,48,0,0,509,511,3,100,50,0,510,508,1,0,0,0,511,514,1,0,0,0,512,
        510,1,0,0,0,512,513,1,0,0,0,513,99,1,0,0,0,514,512,1,0,0,0,515,516,
        5,62,0,0,516,517,5,50,0,0,517,518,3,58,29,0,518,101,1,0,0,0,519,
        520,3,104,52,0,520,521,5,41,0,0,521,522,5,62,0,0,522,103,1,0,0,0,
        523,535,3,74,37,0,524,525,5,41,0,0,525,534,5,62,0,0,526,528,3,80,
        40,0,527,526,1,0,0,0,528,529,1,0,0,0,529,527,1,0,0,0,529,530,1,0,
        0,0,530,534,1,0,0,0,531,532,5,41,0,0,532,534,3,46,23,0,533,524,1,
        0,0,0,533,527,1,0,0,0,533,531,1,0,0,0,534,537,1,0,0,0,535,533,1,
        0,0,0,535,536,1,0,0,0,536,105,1,0,0,0,537,535,1,0,0,0,538,539,5,
        8,0,0,539,540,5,62,0,0,540,541,5,10,0,0,541,543,5,46,0,0,542,544,
        3,108,54,0,543,542,1,0,0,0,544,545,1,0,0,0,545,543,1,0,0,0,545,546,
        1,0,0,0,546,547,1,0,0,0,547,548,5,47,0,0,548,549,5,49,0,0,549,107,
        1,0,0,0,550,551,5,62,0,0,551,553,5,42,0,0,552,554,3,110,55,0,553,
        552,1,0,0,0,553,554,1,0,0,0,554,555,1,0,0,0,555,557,5,43,0,0,556,
        558,3,56,28,0,557,556,1,0,0,0,557,558,1,0,0,0,558,559,1,0,0,0,559,
        560,5,49,0,0,560,109,1,0,0,0,561,566,3,112,56,0,562,563,5,48,0,0,
        563,565,3,112,56,0,564,562,1,0,0,0,565,568,1,0,0,0,566,564,1,0,0,
        0,566,567,1,0,0,0,567,111,1,0,0,0,568,566,1,0,0,0,569,574,5,62,0,
        0,570,571,5,48,0,0,571,573,5,62,0,0,572,570,1,0,0,0,573,576,1,0,
        0,0,574,572,1,0,0,0,574,575,1,0,0,0,575,577,1,0,0,0,576,574,1,0,
        0,0,577,578,3,56,28,0,578,113,1,0,0,0,579,580,7,3,0,0,580,115,1,
        0,0,0,581,582,7,4,0,0,582,117,1,0,0,0,583,584,7,5,0,0,584,119,1,
        0,0,0,585,586,7,6,0,0,586,121,1,0,0,0,587,588,7,7,0,0,588,123,1,
        0,0,0,47,127,137,149,155,168,186,191,205,214,240,244,268,274,282,
        286,294,303,314,318,332,342,353,365,377,389,395,401,417,425,427,
        447,458,469,474,480,482,491,503,512,529,533,535,545,553,557,566,
        574
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'for'", "'return'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
                     "'const'", "'var'", "'continue'", "'break'", "'range'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'", "'&&'", "'||'", "'!'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ADD", 
                      "SUB", "MULTIPLY", "DIVIDE", "REMAIN", "COMPARE_STR", 
                      "NOT_EQ", "GREATER_OR_EQ", "LESS_OR_EQ", "GREATER", 
                      "LESS", "AND", "OR", "NOT", "ASSIGNMENT_SIGN", "SHORT_ADD", 
                      "SHORT_SUB", "SHORT_MULTIPLY", "SHORT_DIVIDE", "SHORT_REMAIN", 
                      "EQUAL", "DOT", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                      "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", 
                      "COMMA", "SEMICOLON", "COLON", "INTEGER_LITERAL", 
                      "DECIMAL_INT", "BINARY_INT", "OCTAL_INT", "HEXA_INT", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "BOOLEAN_LITERAL", 
                      "NIL_LITERAL", "NEWLINE", "WHITESPACE", "IDENTIFIER", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_stmt = 2
    RULE_block = 3
    RULE_var_decl = 4
    RULE_const_decl = 5
    RULE_assign_stmt = 6
    RULE_lhs = 7
    RULE_if_stmt = 8
    RULE_only_if_stmt = 9
    RULE_else_if_list = 10
    RULE_else_stmt = 11
    RULE_for_stmt = 12
    RULE_basic_for_loop = 13
    RULE_for_loop_initial = 14
    RULE_initialization = 15
    RULE_update = 16
    RULE_for_loop_range = 17
    RULE_break_stmt = 18
    RULE_continue_stmt = 19
    RULE_call_stmt = 20
    RULE_return_stmt = 21
    RULE_func_decl = 22
    RULE_func_call = 23
    RULE_argument_list = 24
    RULE_method_decl = 25
    RULE_method_call = 26
    RULE_primitive_type = 27
    RULE_typ = 28
    RULE_expr = 29
    RULE_expr1 = 30
    RULE_expr2 = 31
    RULE_expr3 = 32
    RULE_expr4 = 33
    RULE_expr5 = 34
    RULE_expr6 = 35
    RULE_sub_expr = 36
    RULE_operand = 37
    RULE_array_type = 38
    RULE_array_literal_box = 39
    RULE_array_access_box = 40
    RULE_array_literal = 41
    RULE_array_ele_list = 42
    RULE_array_ele = 43
    RULE_short_array_literal = 44
    RULE_array_access = 45
    RULE_struct_decl = 46
    RULE_struct_field = 47
    RULE_struct_literal = 48
    RULE_struct_ele_list = 49
    RULE_struct_ele = 50
    RULE_struct_access = 51
    RULE_struct_array_method = 52
    RULE_interface_decl = 53
    RULE_interface_method = 54
    RULE_param_list = 55
    RULE_param_decl = 56
    RULE_arith_high_operator = 57
    RULE_arith_low_operator = 58
    RULE_relational_operator = 59
    RULE_assign_operator = 60
    RULE_comment = 61

    ruleNames =  [ "program", "decl", "stmt", "block", "var_decl", "const_decl", 
                   "assign_stmt", "lhs", "if_stmt", "only_if_stmt", "else_if_list", 
                   "else_stmt", "for_stmt", "basic_for_loop", "for_loop_initial", 
                   "initialization", "update", "for_loop_range", "break_stmt", 
                   "continue_stmt", "call_stmt", "return_stmt", "func_decl", 
                   "func_call", "argument_list", "method_decl", "method_call", 
                   "primitive_type", "typ", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "sub_expr", "operand", "array_type", 
                   "array_literal_box", "array_access_box", "array_literal", 
                   "array_ele_list", "array_ele", "short_array_literal", 
                   "array_access", "struct_decl", "struct_field", "struct_literal", 
                   "struct_ele_list", "struct_ele", "struct_access", "struct_array_method", 
                   "interface_decl", "interface_method", "param_list", "param_decl", 
                   "arith_high_operator", "arith_low_operator", "relational_operator", 
                   "assign_operator", "comment" ]

    EOF = Token.EOF
    SINGLE_LINE_COMMENT=1
    MULTI_LINE_COMMENT=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    CONST=15
    VAR=16
    CONTINUE=17
    BREAK=18
    RANGE=19
    ADD=20
    SUB=21
    MULTIPLY=22
    DIVIDE=23
    REMAIN=24
    COMPARE_STR=25
    NOT_EQ=26
    GREATER_OR_EQ=27
    LESS_OR_EQ=28
    GREATER=29
    LESS=30
    AND=31
    OR=32
    NOT=33
    ASSIGNMENT_SIGN=34
    SHORT_ADD=35
    SHORT_SUB=36
    SHORT_MULTIPLY=37
    SHORT_DIVIDE=38
    SHORT_REMAIN=39
    EQUAL=40
    DOT=41
    OPEN_PARENTHESIS=42
    CLOSE_PARENTHESIS=43
    OPEN_BRACKET=44
    CLOSE_BRACKET=45
    OPEN_BRACE=46
    CLOSE_BRACE=47
    COMMA=48
    SEMICOLON=49
    COLON=50
    INTEGER_LITERAL=51
    DECIMAL_INT=52
    BINARY_INT=53
    OCTAL_INT=54
    HEXA_INT=55
    FLOAT_LITERAL=56
    STRING_LITERAL=57
    BOOLEAN_LITERAL=58
    NIL_LITERAL=59
    NEWLINE=60
    WHITESPACE=61
    IDENTIFIER=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.decl()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 98688) != 0)):
                    break

            self.state = 129
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.struct_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.interface_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.func_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def comment(self):
            return self.getTypedRuleContext(MiniGoParser.CommentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.const_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 145
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 146
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 147
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 148
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.stmt()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823719043039342) != 0)):
                    break

            self.state = 157
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(MiniGoParser.VAR)
            self.state = 160
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 161
                self.typ()
                pass

            elif la_ == 2:
                self.state = 162
                self.match(MiniGoParser.EQUAL)
                self.state = 163
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 164
                self.typ()
                self.state = 165
                self.match(MiniGoParser.EQUAL)
                self.state = 166
                self.expr(0)
                pass


            self.state = 170
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.CONST)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
            self.match(MiniGoParser.EQUAL)
            self.state = 175
            self.expr(0)
            self.state = 176
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = MiniGoParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.lhs()
            self.state = 179
            self.assign_operator()
            self.state = 180
            self.expr(0)
            self.state = 181
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lhs)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.struct_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def only_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Only_if_stmtContext,0)


        def else_if_list(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_listContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.only_if_stmt()
            self.state = 189
            self.else_if_list()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 190
                self.else_stmt()


            self.state = 193
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Only_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_only_if_stmt




    def only_if_stmt(self):

        localctx = MiniGoParser.Only_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_only_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.IF)
            self.state = 196
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 197
            self.expr(0)
            self.state = 198
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 199
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def only_if_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Only_if_stmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Only_if_stmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_list




    def else_if_list(self):

        localctx = MiniGoParser.Else_if_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_else_if_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 201
                    self.match(MiniGoParser.ELSE)
                    self.state = 202
                    self.only_if_stmt() 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.ELSE)
            self.state = 209
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_loopContext,0)


        def for_loop_initial(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_initialContext,0)


        def for_loop_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_stmt)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.basic_for_loop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.for_loop_initial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.for_loop_range()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_loop




    def basic_for_loop(self):

        localctx = MiniGoParser.Basic_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.FOR)
            self.state = 217
            self.expr(0)
            self.state = 218
            self.block()
            self.state = 219
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_initialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_initial




    def for_loop_initial(self):

        localctx = MiniGoParser.For_loop_initialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_loop_initial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.FOR)
            self.state = 222
            self.initialization()
            self.state = 223
            self.expr(0)
            self.state = 224
            self.match(MiniGoParser.SEMICOLON)
            self.state = 225
            self.update()
            self.state = 226
            self.block()
            self.state = 227
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_initialization)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.update()
                self.state = 230
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(MiniGoParser.VAR)
                self.state = 233
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 240
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 234
                    self.match(MiniGoParser.EQUAL)
                    self.state = 235
                    self.expr(0)
                    pass
                elif token in [11, 12, 13, 14, 44, 62]:
                    self.state = 236
                    self.typ()
                    self.state = 237
                    self.match(MiniGoParser.EQUAL)
                    self.state = 238
                    self.expr(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 242
                self.match(MiniGoParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 247
            self.assign_operator()
            self.state = 248
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MiniGoParser.FOR)
            self.state = 251
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 252
            self.match(MiniGoParser.COMMA)
            self.state = 253
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 254
            self.match(MiniGoParser.ASSIGNMENT_SIGN)
            self.state = 255
            self.match(MiniGoParser.RANGE)
            self.state = 256
            self.expr(0)
            self.state = 257
            self.block()
            self.state = 258
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.BREAK)
            self.state = 261
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.CONTINUE)
            self.state = 264
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 266
                self.func_call()
                pass

            elif la_ == 2:
                self.state = 267
                self.method_call()
                pass


            self.state = 270
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.RETURN)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823727634579456) != 0):
                self.state = 273
                self.expr(0)


            self.state = 276
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.FUNC)
            self.state = 279
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 280
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 281
                self.param_list()


            self.state = 284
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
                self.state = 285
                self.typ()


            self.state = 288
            self.block()
            self.state = 289
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def argument_list(self):
            return self.getTypedRuleContext(MiniGoParser.Argument_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 292
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5694823727634579456) != 0):
                self.state = 293
                self.argument_list()


            self.state = 296
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_list




    def argument_list(self):

        localctx = MiniGoParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expr(0)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 299
                self.match(MiniGoParser.COMMA)
                self.state = 300
                self.expr(0)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def OPEN_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.OPEN_PARENTHESIS, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def CLOSE_PARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_PARENTHESIS)
            else:
                return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.FUNC)
            self.state = 307
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 308
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 309
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 310
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 311
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 312
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 313
                self.param_list()


            self.state = 316
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
                self.state = 317
                self.typ()


            self.state = 320
            self.block()
            self.state = 321
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.struct_array_method()
            self.state = 324
            self.match(MiniGoParser.DOT)
            self.state = 325
            self.func_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_typ)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.primitive_type()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    self.match(MiniGoParser.OR)
                    self.state = 339
                    self.expr1(0) 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    self.match(MiniGoParser.AND)
                    self.state = 350
                    self.expr2(0) 
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def relational_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 359
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 360
                    self.relational_operator()
                    self.state = 361
                    self.expr3(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def arith_low_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_low_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    self.arith_low_operator()
                    self.state = 373
                    self.expr4(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def arith_high_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Arith_high_operatorContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.arith_high_operator()
                    self.state = 385
                    self.expr5() 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                _la = self._input.LA(1)
                if not(_la==21 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 393
                self.expr5()
                pass
            elif token in [42, 44, 51, 56, 57, 58, 59, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr6)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.struct_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.method_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_sub_expr




    def sub_expr(self):

        localctx = MiniGoParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 404
            self.expr(0)
            self.state = 405
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operand)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 411
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 412
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 414
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 415
                self.func_call()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 416
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_box(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_boxContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_type)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.array_literal_box()
                self.state = 420
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.array_literal_box()
                self.state = 425
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 14]:
                    self.state = 423
                    self.primitive_type()
                    pass
                elif token in [62]:
                    self.state = 424
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_box




    def array_literal_box(self):

        localctx = MiniGoParser.Array_literal_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_array_literal_box)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 430
            _la = self._input.LA(1)
            if not(_la==51 or _la==62):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 431
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_boxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(MiniGoParser.OPEN_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(MiniGoParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access_box




    def array_access_box(self):

        localctx = MiniGoParser.Array_access_boxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_array_access_box)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(MiniGoParser.OPEN_BRACKET)
            self.state = 434
            self.expr(0)
            self.state = 435
            self.match(MiniGoParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def array_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.array_type()
            self.state = 438
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 439
            self.array_ele_list()
            self.state = 440
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele_list




    def array_ele_list(self):

        localctx = MiniGoParser.Array_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.array_ele()
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 443
                self.match(MiniGoParser.COMMA)
                self.state = 444
                self.array_ele()
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(MiniGoParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MiniGoParser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(MiniGoParser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MiniGoParser.STRING_LITERAL, 0)

        def NIL_LITERAL(self):
            return self.getToken(MiniGoParser.NIL_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def short_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Short_array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_ele




    def array_ele(self):

        localctx = MiniGoParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_ele)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(MiniGoParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.FLOAT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.match(MiniGoParser.BOOLEAN_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 453
                self.match(MiniGoParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.match(MiniGoParser.NIL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 455
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 456
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 457
                self.short_array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def array_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_ele_listContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_short_array_literal




    def short_array_literal(self):

        localctx = MiniGoParser.Short_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_short_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 461
            self.array_ele_list()
            self.state = 462
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def array_access_box(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_access_boxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_access_boxContext,i)


        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_access)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.struct_array_method()
                self.state = 469
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.match(MiniGoParser.DOT)
                    self.state = 466
                    self.match(MiniGoParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 467
                    self.match(MiniGoParser.DOT)
                    self.state = 468
                    self.func_call()
                    pass


                self.state = 472 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 471
                        self.array_access_box()

                    else:
                        raise NoViableAltException(self)
                    self.state = 474 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.operand()
                self.state = 478 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 477
                        self.array_access_box()

                    else:
                        raise NoViableAltException(self)
                    self.state = 480 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_struct_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(MiniGoParser.TYPE)
            self.state = 485
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 486
            self.match(MiniGoParser.STRUCT)
            self.state = 487
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 489 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 488
                self.struct_field()
                self.state = 491 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==62):
                    break

            self.state = 493
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 494
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 497
            self.typ()
            self.state = 498
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def struct_ele_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_ele_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 501
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 502
                self.struct_ele_list()


            self.state = 505
            self.match(MiniGoParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_ele_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_ele(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_eleContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_eleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele_list




    def struct_ele_list(self):

        localctx = MiniGoParser.Struct_ele_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_struct_ele_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.struct_ele()
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 508
                self.match(MiniGoParser.COMMA)
                self.state = 509
                self.struct_ele()
                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_ele




    def struct_ele(self):

        localctx = MiniGoParser.Struct_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_struct_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 516
            self.match(MiniGoParser.COLON)
            self.state = 517
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_array_method(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_array_methodContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.struct_array_method()
            self.state = 520
            self.match(MiniGoParser.DOT)
            self.state = 521
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_array_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def func_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Func_callContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Func_callContext,i)


        def array_access_box(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_access_boxContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_access_boxContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_array_method




    def struct_array_method(self):

        localctx = MiniGoParser.Struct_array_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_struct_array_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.operand()
            self.state = 535
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 533
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        self.state = 524
                        self.match(MiniGoParser.DOT)
                        self.state = 525
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        self.state = 527 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 526
                                self.array_access_box()

                            else:
                                raise NoViableAltException(self)
                            self.state = 529 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                        pass

                    elif la_ == 3:
                        self.state = 531
                        self.match(MiniGoParser.DOT)
                        self.state = 532
                        self.func_call()
                        pass

             
                self.state = 537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def OPEN_BRACE(self):
            return self.getToken(MiniGoParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(MiniGoParser.CLOSE_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def interface_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Interface_methodContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_interface_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(MiniGoParser.TYPE)
            self.state = 539
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 540
            self.match(MiniGoParser.INTERFACE)
            self.state = 541
            self.match(MiniGoParser.OPEN_BRACE)
            self.state = 543 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 542
                self.interface_method()
                self.state = 545 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==62):
                    break

            self.state = 547
            self.match(MiniGoParser.CLOSE_BRACE)
            self.state = 548
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(MiniGoParser.OPEN_PARENTHESIS, 0)

        def CLOSE_PARENTHESIS(self):
            return self.getToken(MiniGoParser.CLOSE_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 551
            self.match(MiniGoParser.OPEN_PARENTHESIS)
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 552
                self.param_list()


            self.state = 555
            self.match(MiniGoParser.CLOSE_PARENTHESIS)
            self.state = 557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4611703610613463040) != 0):
                self.state = 556
                self.typ()


            self.state = 559
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Param_declContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.param_decl()
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 562
                self.match(MiniGoParser.COMMA)
                self.state = 563
                self.param_decl()
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_decl




    def param_decl(self):

        localctx = MiniGoParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 570
                self.match(MiniGoParser.COMMA)
                self.state = 571
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 577
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_high_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(MiniGoParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(MiniGoParser.DIVIDE, 0)

        def REMAIN(self):
            return self.getToken(MiniGoParser.REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arith_high_operator




    def arith_high_operator(self):

        localctx = MiniGoParser.Arith_high_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arith_high_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_low_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arith_low_operator




    def arith_low_operator(self):

        localctx = MiniGoParser.Arith_low_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arith_low_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE_STR(self):
            return self.getToken(MiniGoParser.COMPARE_STR, 0)

        def NOT_EQ(self):
            return self.getToken(MiniGoParser.NOT_EQ, 0)

        def GREATER_OR_EQ(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQ, 0)

        def LESS_OR_EQ(self):
            return self.getToken(MiniGoParser.LESS_OR_EQ, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_operator




    def relational_operator(self):

        localctx = MiniGoParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT_SIGN(self):
            return self.getToken(MiniGoParser.ASSIGNMENT_SIGN, 0)

        def SHORT_ADD(self):
            return self.getToken(MiniGoParser.SHORT_ADD, 0)

        def SHORT_SUB(self):
            return self.getToken(MiniGoParser.SHORT_SUB, 0)

        def SHORT_MULTIPLY(self):
            return self.getToken(MiniGoParser.SHORT_MULTIPLY, 0)

        def SHORT_DIVIDE(self):
            return self.getToken(MiniGoParser.SHORT_DIVIDE, 0)

        def SHORT_REMAIN(self):
            return self.getToken(MiniGoParser.SHORT_REMAIN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operator




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.SINGLE_LINE_COMMENT, 0)

        def MULTI_LINE_COMMENT(self):
            return self.getToken(MiniGoParser.MULTI_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_comment




    def comment(self):

        localctx = MiniGoParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.expr_sempred
        self._predicates[30] = self.expr1_sempred
        self._predicates[31] = self.expr2_sempred
        self._predicates[32] = self.expr3_sempred
        self._predicates[33] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




