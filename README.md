# lane-detect
차선감지 학습 과정입니다. 
test1은 rgb이미지에서 흰색을 검출해서 선으로 인식합니다.
test2는 그레이스케일 과정을 거쳐 엣지를 추출하고 관심영역을 설정한 다음 hough변환을 이용하여 차선을 검출 합니다.
test3는 위 과정을 거치지만 선을 여러개 인식할 수도 있으므로 기울기를 구해서 대표선을 추출합니다.
