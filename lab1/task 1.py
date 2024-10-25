numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
mis=numbers.index(None)
sum=sum(numbers[:mis]+numbers[mis+1:])
mid = sum/len(numbers)
numbers[mis]=mid
print("Измененный список:", numbers)
