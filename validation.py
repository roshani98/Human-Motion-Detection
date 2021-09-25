#Linear regression
import numpy as np
import pandas as pd
import math
# zero degree - 12 84 83
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), ((402, 236), 1), (None, 2), ((408, 240), 3), (None, 4), ((403, 246), 5), (None, 6),(None, 7), ((407, 239), 8), (None, 9), (None, 10), ((398, 251), 11), (None, 12), (None, 13), ((398, 252), 14), (None, 15), ((407, 240), 16),(None, 17), ((402, 242), 18), ((407, 237), 19), (None, 20), (None, 21), ((399, 239), 22), ((399, 235), 23), ((399, 229), 24), ((400, 225), 25), ((400, 222), 26), ((401, 217), 27), ((401, 214), 28), (None, 29), (None, 30), ((401, 203), 31), ((401, 201), 32), ((400, 197), 33), ((399, 194), 34), ((398, 188), 35), ((398, 185), 36), ((402, 177), 37), (None, 38), (None, 39), ((398, 174), 40), ((398, 171), 41), ((398, 168), 42), (None, 43), ((396, 159), 44), (None, 45), (None, 46), (None, 47), (None, 48), ((394, 145), 49), (None, 50), ((393, 137), 51), (None, 52),(None, 53), (None, 54), ((391, 125), 55), (None, 56), ((390, 118), 57), ((390, 116), 58), (None, 59), (None, 60), (None, 61), (None, 62), ((389, 100), 63), (None, 64), (None, 65), (None, 66), ((393, 82), 67), ((387, 83), 68), ((386, 80), 69), (None, 70), ((387, 75), 71), (None, 72), ((385, 69), 73), (None, 74), (None, 75), (None, 76), (None, 77), (None, 78), ((380, 51), 79), ((380, 49), 80), (None, 81), ((385, 41), 82), ((379, 41), 83), (None, 84)], [379, 41]), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0), ((361, 223), 1), (None, 2), (None, 3), ((366, 218), 4), (None, 5), ((357, 218), 6), ((360, 223), 7), (None, 8), ((362, 213), 9), ((362, 213), 10), ((360, 224), 11), (None, 12), (None,13), (None, 14), ((359, 225), 15), ((365, 219), 16), ((365, 219), 17), (None, 18), (None, 19), ((359, 222), 20), (None, 21), ((360, 207), 22), ((355, 208), 23), ((364, 202), 24), ((365, 199), 25), ((359, 202), 26), (None, 27), ((365, 191), 28), ((359, 194), 29), ((358, 180), 30), (None, 31), ((363, 180), 32), (None, 33), (None, 34), ((356, 162), 35), ((356, 159), 36), ((357, 166), 37), (None, 38), (None, 39), ((361, 151), 40), ((357, 144), 41), (None, 42), (None, 43), (None, 44), (None, 45), (None, 46), (None, 47), (None, 48), (None, 49), (None, 50), (None,51), (None, 52), ((358, 105), 53), (None, 54), ((358, 99), 55), ((358, 95), 56), (None, 57), (None, 58), (None, 59), ((354, 89), 60), ((349,82), 61), (None, 62), (None, 63), (None, 64), (None, 65), ((354, 67), 66), (None, 67), ((353, 60), 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), ((355, 32), 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), (None, 82), (None, 83), ((352, 8), 84)], [352, 8])}

#60 degree - 61 53 66
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [ (None, 29), (None, 30), (None, 31), (None, 32), (None, 33), (None, 34), (None, 35), (None, 36), (None, 37),(None, 38), ((427, 239), 39), (None, 40), (None, 41), (None, 42), (None, 43), ((426, 232), 44), (None, 45), (None, 46), (None, 47), (None, 48), (None, 49), (None, 50), (None, 51), (None, 52), (None, 53), ((426, 215), 54), ((424, 207), 55), (None, 56), (None, 57), (None, 58), ((423, 206), 59), (None, 60), ((428, 194), 61), (None, 62), ((429, 191), 63), (None, 64), (None, 65), (None, 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), (None, 75), ((441, 172), 76), (None, 77), (None, 78), (None, 79), (None, 80),(None, 81), (None, 82), (None, 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), ((439, 152), 89), (None, 90), (None, 91), (None, 92), (None, 93), (None, 94), (None, 95), ((453, 138), 96), (None, 97), (None, 98), (None, 99), (None, 100), (None, 101), (None, 102), ((459, 125), 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108), (None, 109), ((478, 102), 110), (None, 111), (None, 112), (None, 113), (None, 114), ((473, 96), 115), (None, 116), (None, 117), (None, 118), (None, 119), (None, 120), (None, 121), (None, 122), (None, 123), (None, 124), (None, 125), (None, 126), (None, 127), (None, 128), (None, 129), (None, 130), (None, 131), (None, 132), (None, 133), (None, 134), (None, 135), (None, 136)], [473, 96]), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0), (None, 1), ((375, 234), 2), (None, 3), ((376, 234), 4), ((375, 234), 5), (None, 6), ((381, 234), 7), (None, 8), (None, 9), (None, 10), (None, 11), ((375, 235), 12), ((375, 234), 13), ((374, 234), 14), (None, 15), ((375, 235), 16), ((381, 233), 17), (None, 18), (None, 19), (None, 20), ((381, 234), 21), ((374, 235), 22), ((368, 235), 23), ((374, 236), 24), ((373, 237), 25), ((373, 235), 26), ((372, 233), 27), ((370, 232), 28), (None, 29), ((375, 235), 30), ((366, 234), 31), (None, 32), ((370, 226), 33), ((354, 220), 34), ((353, 218), 35), (None, 36), (None, 37), ((361, 210), 38), ((347, 209), 39), ((346, 208), 40), (None, 41), (None, 42), (None, 43), ((342, 199), 44), ((341, 198), 45), (None, 46), ((341, 194), 47), (None, 48), (None, 49), (None, 50), (None, 51), (None, 52), (None, 53), (None, 54), (None, 55), (None, 56), (None, 57), (None, 58), (None, 59), (None, 60), (None,61), (None, 62), (None, 63), (None, 64), (None, 65), (None, 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), ((293, 126), 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), ((291, 114), 81), ((284, 112), 82), ((287,109), 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), (None, 90), ((273, 89), 91), (None, 92), (None, 93), (None, 94), (None, 95), (None, 96), ((258, 80), 97), (None, 98), (None, 99), (None, 100), (None, 101), (None, 102), ((254, 72), 103), ((253, 70),104), (None, 105), ((254, 63), 106), (None, 107), ((249, 59), 108), (None, 109), ((245, 55), 110), (None, 111), ((241, 53), 112), (None, 113), (None, 114), ((234, 48), 115), ((232, 45), 116), (None, 117), ((230, 44), 118), (None, 119), (None, 120), ((228, 42), 121), (None, 122), ((226, 40), 123), ((225, 40), 124), (None, 125), ((220, 42), 126), (None, 127), (None, 128), ((225, 37), 129), (None, 130), ((226, 38), 131), (None, 132), ((225, 38), 133), (None, 134), (None, 135), (None, 136)], [225, 38])}

#100 degree - 96 36 48
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), (None, 1), (None, 2), (None, 3), (None, 4), (None, 5), (None, 6), ((403, 249), 7), (None, 8), (None, 9), ((403, 250), 10), (None, 11), ((398, 254), 12), ((398, 254), 13), (None, 14), (None, 15), (None, 16), (None, 17), (None, 18), ((407, 244), 19), (None, 20), (None, 21), ((404, 241), 22), ((411, 236), 23), ((405, 239), 24), ((413, 232), 25), ((414, 228), 26), (None, 27), ((416, 222), 28), ((418, 219), 29), (None, 30), ((421, 216), 31), (None, 32), ((426, 209), 33), (None, 34), (None, 35), ((433, 200), 36), (None, 37), ((437, 195), 38), ((431, 196), 39), ((439, 192), 40), ((434, 191), 41), (None, 42), ((444, 183), 43), (None, 44), (None, 45), (None, 46), ((453, 173), 47), (None, 48), (None, 49), (None, 50), ((466, 164), 51), (None, 52), (None, 53), (None, 54), (None, 55), ((475, 155), 56), (None, 57), (None, 58), ((482, 150), 59), (None, 60), ((486, 147), 61), (None, 62), (None, 63), (None, 64), (None, 65), ((491, 142), 66), ((493, 140), 67), (None, 68), (None, 69), ((498, 132), 70), (None, 71), (None, 72), (None, 73), (None, 74), (None, 75), ((502, 122), 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), ((518, 112), 82), (None, 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), (None, 90), (None, 91), (None, 92), (None, 93), (None, 94), ((542, 82), 95), (None, 96), (None, 97), (None, 98), (None, 99), ((557, 79), 100), (None, 101), (None, 102), (None, 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108), (None, 109), (None, 110), (None, 111), (None, 112)], [557, 79]), 'left_wrist': ((0, 255, 0), (255, 255, 0), [((360, 232), 0), ((367, 226), 1), ((367, 227), 2), ((367, 227), 3), ((371, 233), 4), ((360, 230), 5), ((370, 233), 6), ((371, 234), 7), ((365, 236), 8), (None, 9), ((361, 232), 10), (None, 11), ((360, 232), 12), ((370, 233), 13), (None, 14), (None, 15), ((364, 237), 16), ((369, 232), 17), ((362, 236), 18), ((357, 229), 19), ((361, 223), 20), ((360, 221), 21), ((357, 218), 22), (None, 23), (None, 24), ((348, 220), 25), ((345, 219), 26), ((340, 211), 27), ((340, 215), 28), (None, 29), ((330, 205), 30), ((327, 202), 31), (None, 32), ((329, 198), 33), ((315, 194), 34), ((321, 194), 35), (None, 36), (None, 37), ((297, 184), 38), ((300, 179), 39), ((296, 176), 40), ((290, 183), 41), ((294, 178), 42), ((280, 173), 43), (None, 44), ((274, 170), 45), ((271, 167), 46), ((273, 172), 47), ((273, 160), 48), (None, 49), (None, 50), (None, 51), (None, 52), ((257, 155), 53), ((258, 159), 54), ((262, 152), 55), (None, 56), (None, 57), ((245, 145), 58), ((253, 145), 59), (None, 60), ((238, 140), 61), (None, 62), ((236, 137), 63), ((235, 136), 64), (None, 65), (None, 66), (None, 67), ((233, 136), 68), ((231, 135), 69), ((240, 136), 70), (None, 71), ((227, 131), 72), ((235, 131), 73), ((229, 125), 74), ((221, 128), 75), (None, 76), (None, 77), (None, 78), ((223, 122), 79), ((221, 122), 80), ((212, 124), 81), (None, 82), ((205, 115), 83), ((214, 115), 84), (None, 85), ((198, 112), 86), (None, 87), ((193, 109), 88), (None, 89), ((198, 107), 90), ((192, 101), 91), ((192, 100), 92), ((185, 104), 93), ((196, 105), 94), ((190, 99), 95), (None, 96), (None, 97), ((182, 101), 98), ((184, 93),99), ((177, 96), 100), (None, 101), ((187, 95), 102), ((176, 94), 103), (None, 104), (None, 105), ((179, 87), 106), (None, 107), (None, 108), (None, 109), (None, 110), ((170, 88), 111), ((175, 84), 112)], [175, 84])}

#140 degree - 144.123 
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), ((414, 241), 1), (None, 2), ((414, 241), 3), ((407, 245), 4), ((407, 245), 5), ((407, 244), 6), ((414, 240), 7), ((413, 240), 8), ((407, 243), 9), ((413, 239), 10), ((413, 239), 11), ((414, 239), 12), ((413, 240), 13), ((407, 246), 14), ((413, 243), 15), ((407, 247), 16), ((407, 245), 17), ((413, 242), 18), ((407, 245), 19), ((407, 245), 20), ((407, 245), 21), ((413, 243), 22), ((413, 245), 23), ((407, 248), 24), (None, 25), ((408, 245), 26), ((416, 239), 27), ((412, 241), 28), (None, 29), (None, 30),(None, 31), (None, 32), (None, 33), (None, 34), (None, 35), ((438, 232), 36), ((440, 231), 37), (None, 38), (None, 39), (None, 40), (None, 41), (None, 42), (None, 43), (None, 44), (None, 45), ((458, 221), 46), (None, 47), (None, 48), (None, 49), (None, 50), (None, 51), (None, 52),(None, 53), ((476, 211), 54), ((478, 210), 55), (None, 56), (None, 57), (None, 58), (None, 59), (None, 60), (None, 61), (None, 62), (None, 63), (None, 64), (None, 65), (None, 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), (None, 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), (None, 82), (None, 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), (None, 90), (None, 91), (None, 92), (None, 93), (None, 94), (None, 95), ((572, 179), 96), (None, 97), (None, 98), (None, 99), (None, 100), (None, 101), (None, 102), (None, 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108), (None, 109), (None, 110), (None, 111), (None, 112), (None, 113), (None, 114)], [572, 179]), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0),((376, 232), 1), (None, 2), ((365, 228), 3), ((369, 236), 4), ((376, 232), 5), ((365, 230), 6), ((365, 229), 7), ((369, 234), 8), ((376, 230), 9), (None, 10), ((365, 228), 11), ((375, 229), 12), ((369, 235), 13), ((371, 227), 14), ((365, 233), 15), ((369, 238), 16), ((375, 233), 17), ((369, 237), 18), ((375, 232), 19), ((375, 232), 20), ((372, 227), 21), ((365, 233), 22), ((368, 240), 23), ((370, 229), 24), ((360, 233), 25), ((370, 235), 26), ((368, 235), 27), ((357, 232), 28), ((366, 234), 29), ((361, 227), 30), (None, 31), ((349, 229), 32), ((346, 227), 33), ((353, 228), 34), ((339, 224), 35), ((343, 220), 36), ((338, 229), 37), (None, 38), ((329, 222), 39), ((331, 227), 40), ((336, 223), 41),(None, 42), ((320, 220), 43), (None, 44), ((325, 221), 45), ((311, 219), 46), ((318, 219), 47), (None, 48), ((303, 216), 49), ((312, 218), 50), (None, 51), ((306, 215), 52), ((297, 219), 53), (None, 54), ((295, 212), 55), ((281, 210), 56), ((278, 210), 57), (None, 58), ((278, 204), 59), (None, 60), ((270, 202), 61), ((260, 205), 62), ((263, 200), 63), ((253, 204), 64), (None, 65), ((250, 207), 66), ((243, 201), 67), (None, 68), ((238, 200), 69), ((245, 199), 70), (None, 71), (None, 72), ((237, 197), 73), ((224, 197), 74), (None, 75), ((218, 196), 76), ((227, 196), 77), ((213, 196), 78), ((210, 195), 79), ((206, 194), 80), ((213, 193), 81), ((209, 193), 82), ((201, 187), 83), ((198, 197), 84), ((201, 192), 85), (None, 86), ((186, 191), 87), ((190, 195), 88), ((189, 196), 89), ((195, 190), 90), (None, 91), ((185, 194), 92), (None, 93),((188, 188), 94), ((182, 194), 95), ((181, 194), 96), ((187, 188), 97), ((186, 188), 98), ((186, 188), 99), ((185, 188), 100), (None, 101), ((186, 188), 102), ((185, 189), 103), ((185, 189), 104), ((185, 189), 105), ((174, 190), 106), (None, 107), (None, 108), ((179, 185), 109), ((185, 189), 110), (None, 111), ((184, 190), 112), ((184, 190), 113), ((184, 190), 114)], [184, 190])}

#180 degree
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), (None, 1), ((409, 245), 2), ((409, 245), 3), (None, 4), (None, 5), (None, 6), ((412, 245), 7), ((412, 245), 8), (None, 9), (None, 10), (None, 11), (None, 12), ((413, 245), 13), ((413, 244), 14), ((413, 243), 15), (None, 16),(None, 17), (None, 18), ((416, 245), 19), (None, 20), (None, 21), (None, 22), (None, 23), (None, 24), ((427, 244), 25), ((429, 244), 26), ((429, 243), 27), ((431, 242), 28), (None, 29), ((439, 237), 30), (None, 31), (None, 32), ((438, 242), 33), (None, 34), (None, 35), (None, 36),(None, 37), (None, 38), ((447, 242), 39), ((449, 242), 40), (None, 41), (None, 42), (None, 43), (None, 44), ((458, 243), 45), (None, 46), (None, 47), (None, 48), (None, 49), (None, 50), ((468, 242), 51), (None, 52), (None, 53), (None, 54), (None, 55), (None, 56), (None, 57), (None, 58), ((485, 241), 59), ((487, 241), 60), (None, 61), (None, 62), (None, 63), (None, 64), (None, 65), ((500, 243), 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), ((526, 244), 72), ((530, 244), 73), (None, 74), (None, 75), ((542, 243), 76), (None, 77), (None, 78),(None, 79), (None, 80), (None, 81), (None, 82), (None, 83), (None, 84), (None, 85), ((570, 239), 86), (None, 87), (None, 88), (None, 89), (None, 90), (None, 91), (None, 92), (None, 93), (None, 94), (None, 95), (None, 96), (None, 97), (None, 98), (None, 99), (None, 100), (None, 101)], [570, 239]), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0), ((361, 239), 1), (None, 2), ((366, 243), 3), ((366, 243), 4), ((360, 238), 5), ((367, 233), 6), ((360, 239), 7), (None, 8), ((360, 240), 9), ((360, 239), 10), ((360, 239), 11), ((360, 238), 12), (None, 13), ((360, 238), 14), ((370, 237), 15), ((360, 238), 16), ((370, 238), 17), ((370, 239), 18), (None, 19), (None, 20), ((364, 244), 21), ((358, 238),22), ((366, 238), 23), ((355, 237), 24), ((351, 238), 25), (None, 26), ((348, 238), 27), ((346, 238), 28), ((344, 238), 29), ((342, 239), 30), ((339, 239), 31), ((337, 239), 32), (None, 33), ((331, 240), 34), ((340, 241), 35), ((337, 241), 36), (None, 37), ((326, 236), 38), ((328,242), 39), ((325, 242), 40), ((322, 242), 41), ((310, 243), 42), ((320, 243), 43), (None, 44), ((311, 239), 45), ((313, 244), 46), ((304, 249), 47), ((301, 249), 48), ((306, 244), 49), ((304, 244), 50), ((303, 245), 51), (None, 52), (None, 53), ((284, 245), 54), (None, 55), ((285,250), 56), (None, 57), ((280, 250), 58), ((278, 250), 59), ((281, 246), 60), (None, 61), (None, 62), (None, 63), ((262, 247), 64), ((265, 242), 65), (None, 66), ((265, 247), 67), ((257, 243), 68), (None, 69), ((250, 243), 70), (None, 71), (None, 72), ((238, 246), 73), (None, 74), (None, 75), ((224, 252), 76), ((234, 252), 77), (None, 78), ((232, 252), 79), ((231, 252), 80), ((230, 253), 81), (None, 82), ((226, 253), 83), ((224, 254), 84), ((215, 259), 85), (None, 86), (None, 87), ((209, 259), 88), ((214, 254), 89), ((207, 249), 90), ((210, 254), 91), ((203,250), 92), (None, 93), ((204, 255), 94), ((202, 255), 95), ((196, 250), 96), ((199, 255), 97), ((199, 255), 98), (None, 99), ((196, 255), 100), (None, 101)], [196, 255])}

#slowest
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), (None, 1), (None, 2), (None, 3), (None, 4), (None, 5), (None, 6), (None, 7), (None,8), (None, 9), (None, 10), (None, 11), (None, 12), (None, 13), (None, 14), (None, 15), (None, 16), (None, 17), (None, 18), (None, 19), (None, 20), (None, 21), (None, 22), (None, 23), (None, 24), (None, 25), (None, 26), (None, 27), (None, 28), (None, 29), (None, 30), (None, 31), (None, 32), (None, 33), (None, 34), (None, 35), (None, 36), (None, 37), (None, 38), (None, 39), (None, 40), (None, 41), (None, 42), (None, 43),(None, 44), (None, 45), (None, 46), (None, 47), (None, 48), (None, 49), (None, 50), (None, 51), (None, 52), (None, 53), (None, 54), (None, 55), (None, 56), (None, 57), (None, 58), (None, 59), (None, 60), (None, 61), (None, 62), (None, 63), (None, 64), (None, 65), (None, 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), (None, 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), (None, 82), (None, 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), (None, 90),(None, 91), (None, 92), (None, 93), (None, 94), (None, 95), (None, 96), (None, 97), (None, 98), (None, 99), (None, 100), (None, 101), (None,102), (None, 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108), (None, 109), (None, 110), (None, 111), (None, 112), (None, 113), (None, 114), (None, 115), (None, 116), (None, 117), (None, 118), (None, 119), (None, 120), (None, 121), (None, 122), (None, 123), (None, 124), (None, 125), (None, 126), (None, 127), (None, 128), (None, 129), (None, 130), (None, 131), (None, 132), (None, 133), (None, 134), (None, 135), (None, 136), (None, 137), (None, 138), (None, 139), (None, 140), (None, 141), (None, 142), (None, 143), (None, 144), (None, 145), (None, 146), (None, 147), (None, 148), (None, 149), (None, 150), (None, 151), (None, 152), (None, 153), (None, 154), (None, 155), (None, 156), (None, 157), (None, 158), (None, 159), (None, 160), (None, 161), (None, 162), (None, 163), (None, 164), (None, 165), (None, 166), (None, 167), (None, 168), (None, 169), (None, 170), (None, 171), (None, 172), (None, 173), (None, 174), (None, 175), (None, 176), (None, 177), (None, 178), (None, 179), (None, 180), (None, 181), (None, 182), (None, 183), (None, 184), (None, 185), (None, 186), (None, 187), (None, 188), (None, 189), (None, 190), (None, 191), (None, 192), (None, 193), (None, 194), (None, 195), (None, 196), (None, 197), (None, 198), (None, 199), (None, 200), (None, 201), (None, 202), (None, 203), (None, 204), (None, 205), (None, 206), (None, 207), (None, 208), (None, 209), (None, 210),(None, 211), (None, 212), (None, 213), (None, 214), (None, 215), (None, 216), (None, 217), (None, 218), (None, 219), (None, 220), (None, 221), (None, 222), (None, 223), (None, 224), (None, 225), (None, 226), (None, 227), (None, 228), (None, 229), (None, 230), (None, 231), (None, 232), (None, 233)], []), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0), (None, 1), ((572, 231), 2), (None, 3), (None, 4), ((563, 219),5), ((566, 232), 6), ((562, 226), 7), ((558, 220), 8), ((568, 230), 9), ((557, 226), 10), ((556, 226), 11), ((557, 233), 12), ((553, 220), 13), ((553, 226), 14), ((550, 220), 15), ((549, 219), 16), ((558, 230), 17), ((547, 226), 18), ((546, 226), 19), ((547, 233), 20), ((544, 226), 21), ((542, 220), 22), ((541, 226), 23), ((540, 226), 24), ((539, 226), 25), ((534, 219), 26), ((532, 219), 27), (None, 28), ((529, 227), 29), ((530, 234), 30), ((526, 227), 31), ((525, 227), 32), ((525, 233), 33), ((520, 226), 34), ((518, 227), 35), (None, 36), (None, 37), ((516, 234), 38), ((519, 224), 39), (None, 40), ((511, 234), 41), ((508, 227), 42), (None, 43), ((505, 227), 44), ((503, 227), 45), ((501, 227), 46), ((502, 232), 47), ((498, 227), 48), ((507, 232), 49), ((497, 228), 50), (None, 51), ((503, 233), 52), ((492, 228), 53), ((499, 226), 54),((492, 236), 55), (None, 56), ((496, 234), 57), ((484, 229), 58), ((485, 237), 59), ((484, 237), 60), ((490, 235), 61), (None, 62), (None, 63), ((478, 238), 64), (None, 65), (None, 66), ((471, 226), 67), ((470, 232), 68), ((468, 233), 69), ((468, 240), 70), (None, 71), ((472, 238), 72), ((464, 235), 73), ((468, 232), 74), ((466, 232), 75), (None, 76), ((464, 240), 77), ((463, 240), 78), ((454, 242), 79), ((454, 242), 80), (None, 81), ((458, 240), 82), ((454, 233), 83), ((444, 236), 84), (None, 85), ((450, 241), 86), (None, 87), (None, 88), ((437, 237), 89),((444, 242), 90), ((442, 241), 91), ((440, 242), 92), ((429, 237), 93), (None, 94), ((434, 242), 95), ((431, 242), 96), ((418, 238), 97), (None, 98), ((417, 245), 99), ((420, 236), 100), ((421, 242), 101), ((410, 237), 102), ((409, 237), 103), ((410, 245), 104), ((412, 235), 105),((412, 241), 106), ((411, 242), 107), ((409, 241), 108), ((408, 241), 109), (None, 110), ((404, 240), 111), ((402, 241), 112), ((392, 244), 113), ((390, 244), 114), ((395, 242), 115), (None, 116), (None, 117), ((391, 243), 118), ((389, 243), 119), ((387, 243), 120), ((385, 242), 121), ((384, 242), 122), ((375, 239), 123), ((381, 242), 124), ((373, 245), 125), ((378, 242), 126), ((376, 242), 127), ((365, 238), 128), (None, 129), ((369, 243), 130), (None, 131), (None, 132), ((358, 244), 133), ((360, 234), 134), ((354, 244), 135), ((351, 238), 136), ((352, 244), 137), ((349, 244), 138), ((354, 241), 139), ((350, 235), 140), ((349, 241), 141), ((347, 241), 142), ((345, 242), 143), (None, 144), ((342, 242), 145), ((340, 241), 146), ((333, 244), 147), ((338, 241), 148), ((330, 244), 149), ((329, 244), 150), ((327, 245), 151), ((334, 241), 152), ((332, 241), 153), ((331, 241), 154), ((329, 241), 155), ((328, 241), 156), ((326, 241), 157), ((326, 241), 158), (None, 159), ((323, 241), 160), ((322, 242), 161), ((320, 241), 162), (None, 163), ((318, 242), 164), ((310, 245), 165), ((308, 245), 166), (None, 167), ((312, 243), 168), ((311, 243), 169), ((309, 243), 170), ((301, 247), 171), ((299, 247), 172), (None, 173), ((303, 243), 174), ((302, 243), 175), ((300, 243), 176), ((293, 247), 177), ((298, 243), 178), ((289, 247), 179), ((288, 247), 180), ((286, 247), 181), ((284, 248), 182), ((288, 244),183), (None, 184), ((285, 244), 185), ((283, 244), 186), ((282, 244), 187), ((280, 244), 188), ((272, 247), 189), ((275, 243), 190), ((273, 243), 191), ((264, 247), 192), (None, 193), ((261, 247), 194), (None, 195), ((263, 244), 196), (None, 197), ((257, 245), 198), ((249, 249), 199), ((253, 245), 200), ((252, 245), 201), (None, 202), ((250, 245), 203), ((249, 245), 204), ((240, 249), 205), ((239, 249), 206), ((244, 245), 207), ((236, 249), 208), ((235, 249), 209), ((229, 244), 210), ((232, 249), 211), ((238, 246), 212), ((230, 250), 213), ((228, 250), 214), ((226, 250), 215), ((224, 250), 216), ((228, 247), 217), ((227, 247), 218), ((222, 242), 219), (None, 220), ((212, 246), 221), (None, 222),((222, 248), 223), (None, 224), ((219, 248), 225), (None, 226), ((203, 247), 227), ((211, 249), 228), ((208, 249), 229), ((207, 249), 230), (None, 231), ((205, 250), 232), ((203, 251), 233)], [203, 251])}

#medium
#body_points = {'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), (None, 1), (None, 2), (None, 3), (None, 4), (None, 5), (None, 6), (None, 7), (None,8), (None, 9), (None, 10), (None, 11), (None, 12), (None, 13), (None, 14), (None, 15), (None, 16), (None, 17), (None, 18), (None, 19), (None, 20), (None, 21), (None, 22), (None, 23), (None, 24), (None, 25), (None, 26), (None, 27), (None, 28), (None, 29), (None, 30), (None, 31), (None, 32), (None, 33), (None, 34), (None, 35), (None, 36), (None, 37), (None, 38), (None, 39), (None, 40), (None, 41), (None, 42), (None, 43),(None, 44), (None, 45), (None, 46), (None, 47), (None, 48), (None, 49), (None, 50), (None, 51), (None, 52), (None, 53), (None, 54), (None, 55), (None, 56), (None, 57), (None, 58), (None, 59), (None, 60), (None, 61), (None, 62), (None, 63), (None, 64), (None, 65), (None, 66), (None, 67), (None, 68), (None, 69), (None, 70), (None, 71), (None, 72), (None, 73), (None, 74), (None, 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), (None, 82), (None, 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), (None, 90),(None, 91), (None, 92), (None, 93), (None, 94), (None, 95), (None, 96), (None, 97), (None, 98), (None, 99), (None, 100), (None, 101), (None,102), (None, 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108)], []), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None,0), ((557, 226), 1), ((554, 233), 2), (None, 3), ((544, 232), 4), (None, 5), ((537, 226), 6), ((535, 227), 7), ((533, 227), 8), ((529, 227),9), (None, 10), ((525, 233), 11), ((523, 234), 12), (None, 13), (None, 14), (None, 15), ((511, 227), 16), ((510, 234), 17), ((508, 234), 18), (None, 19), (None, 20), (None, 21), (None, 22), ((495, 227), 23), (None, 24), (None, 25), ((486, 232), 26), ((484, 232), 27), ((480, 233), 28), (None, 29), (None, 30), ((469, 233), 31), ((467, 241), 32), (None, 33), (None, 34), ((454, 237), 35), ((451, 237), 36), (None, 37), (None, 38), ((440, 237), 39), ((437, 237), 40), ((434, 237), 41), ((431, 237), 42), (None, 43), ((424, 237), 44), ((421, 238), 45), (None, 46), (None, 47), ((409, 239), 48), (None, 49), ((402, 240), 50), (None, 51), ((395, 239), 52), ((393, 240), 53), ((390, 240), 54), ((388, 240), 55), (None, 56), ((382, 239), 57), ((376, 233), 58), (None, 59), (None, 60), (None, 61), (None, 62), (None, 63), ((353, 236), 64), (None, 65), (None, 66), ((344, 235), 67), ((342, 241), 68), (None, 69), ((337, 243), 70), ((333, 242), 71), (None, 72), ((327, 237), 73), (None, 74), ((323, 244), 75), (None, 76), (None, 77), (None, 78), (None, 79), (None, 80), (None, 81), ((294, 242), 82), ((293, 247), 83), (None, 84), (None, 85), (None, 86), (None, 87), (None, 88), (None, 89), ((262, 242), 90), (None, 91), (None, 92), (None, 93), (None, 94), ((242, 244), 95), (None, 96), (None, 97), ((230, 244), 98), (None, 99), (None, 100), (None, 101), (None, 102), ((202, 254), 103), (None, 104), (None, 105), (None, 106), (None, 107), (None, 108)], [202, 254])}

#fast
#{'right_wrist': ((0, 255, 255), (255, 0, 0), [(None, 0), (None, 1), (None, 2), (None, 3), (None, 4), (None, 5), (None, 6), (None, 7), (None,8), (None, 9), (None, 10), (None, 11), (None, 12), (None, 13), (None, 14), (None, 15), (None, 16), (None, 17), (None, 18), (None, 19), (None, 20), (None, 21), (None, 22), (None, 23), (None, 24), (None, 25), (None, 26), (None, 27), (None, 28), (None, 29), (None, 30), (None, 31), (None, 32), (None, 33), (None, 34), (None, 35)], []), 'left_wrist': ((0, 255, 0), (255, 255, 0), [(None, 0), (None, 1), ((471, 234), 2), (None,3), ((441, 239), 4), (None, 5), (None, 6), ((412, 233), 7), ((405, 240), 8), (None, 9), ((390, 240), 10), ((376, 242), 11), ((366, 238), 12), ((359, 244), 13), (None, 14), ((330, 241), 15), (None, 16), ((307, 246), 17), (None, 18), (None, 19), (None, 20), (None, 21), (None, 22), ((233, 243), 23), (None, 24), ((214, 245), 25), (None, 26), (None, 27), (None, 28), (None, 29), (None, 30), (None, 31), (None, 32), (None, 33), (None, 34), (None, 35)], [214, 245])}


right = body_points['right_wrist'][2]
left = body_points['left_wrist'][2]
rw = []
lw = []
for i in right:
    if(i[0] != None):
        rw.append(i[0])
for i in left:
   if(i[0] != None):
           lw.append(i[0])
        
data_r  = np.asarray(rw)
data_l = np.asarray(lw)
print("data_r shape : ", data_r.shape)
print("data_l shape : ", data_l.shape)

# y = theta0 + theta1*x


X_r = data_r[:,0]
X_r = X_r[:,np.newaxis]
o = np.ones((X_r.shape[0],1))
X_r = np.hstack((o,X_r))

y_r = data_r[:,1]
y_r = y_r[:,np.newaxis]

X_l = data_l[:,0]
X_l = X_l[:,np.newaxis]
o = np.ones((X_l.shape[0],1))
X_l = np.hstack((o,X_l))

y_l = data_l[:,1] 
y_l = y_l[:,np.newaxis]

#theta = (X.T * X)^-1 * X.T * y
theta_r = np.dot(np.dot(np.linalg.pinv(np.dot(X_r.T,X_r)),X_r.T),y_r)
theta_l = np.dot(np.dot(np.linalg.pinv(np.dot(X_l.T,X_l)),X_l.T),y_l)
if(math.atan(theta_r[1])*180/np.pi > 0):
    diff = -math.atan(theta_r[1])*180/np.pi + math.atan(theta_l[1])*180/np.pi
else:
    diff = 180 + math.atan(theta_r[1])*180/np.pi - math.atan(theta_l[1])*180/np.pi
#print("180 degree")
print(math.atan(theta_r[1])*180/np.pi)
print(math.atan(theta_l[1])*180/np.pi)
print(diff)