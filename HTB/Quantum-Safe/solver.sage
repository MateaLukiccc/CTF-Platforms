######################################################################## knowns

M = Matrix(ZZ, [
    [47, -77, -85],
    [-49, 78, 50],
    [57, -78, 99]
])

CT = [(-981, 1395, -1668), (6934, -10059, 4270), (3871, -5475, 3976), (4462, -7368, -8954), (2794, -4413, -3461), (5175, -7518, 3201), (3102, -5051, -5457), (7255, -10884, -266), (5694, -8016, 6237), (4160, -6038, 2582), (4940, -7069, 3770), (3185, -5158, -4939), (7669, -11686, -2231), (5601, -9013, -7971), (5600, -8355, 575), (1739, -2838, -3037), (2572, -4120, -3788), (8055, -11985, 1137), (7088, -10247, 5141), (8384, -12679, -1381), (-785, 1095, -1841), (4250, -6762, -5242), (3716, -5364, 2126), (5673, -7968, 6741), (5877, -9190, -4803), (5639, -8865, -5356), (1980, -3230, -3366), (6183, -9334, -1002), (2575, -4068, -2828), (7521, -11374, -1137), (5639, -8551, -1501), (4194, -6039, 3213), (2072, -3025, 383), (2444, -3699, -502), (6313, -9653, -2447), (4502, -7090, -4435), (-421, 894, 2912), (4667, -7142, -2266), (4228, -6616, -3749), (6258, -9719, -4407), (6044, -9561, -6463), (266, -423, -637), (3849, -6223, -5988), (5809, -9021, -4115), (4794, -7128, 918), (6340, -9442, 892), (5322, -8614, -8334)]

#################################################################### decryption

inv = M.inverse()
deltas = [(vector(c) - vector(CT[0])) * inv for c in CT]
flag = ''.join([chr(ord('H') + d[0]) for d in deltas])
print(flag)