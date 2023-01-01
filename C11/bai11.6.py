chieu_cao=[74,74,72,72,73,69,69,71,76,71]
chieu_cao2=[round(x*0.0245,2) for x in chieu_cao ]
print("3 chiều cao đầu",chieu_cao2[0:3])
print("3 chiều cao cuối",chieu_cao2[-3:])
print("chiều cao trung bình",sum(chieu_cao2)/(len(chieu_cao2)))
chieu_cao2.sort()
print("chiều cao tăng dần",chieu_cao2)
chieu_cao2.reverse()
print("chiều cao giảm dần",chieu_cao2)