#playlist=["zen","blank space","one ofthe girls"]
# fav_food=["dosa","rasam","mushroom"]

# playlist.append("killing it girl")
# print(playlist)

# playlist.insert(2,"like")
# print(playlist)

# playlist.remove("zen")
# print(playlist)

# playlist.pop()

#numbers=[10,100,32,874,207,50,100,37,90]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.count(100))
# print(numbers[1])
# numbers[1]=50
# print(numbers[1])
# print(numbers[0:3])
# print(numbers[-2:])
# for num in numbers:
#     print(num)

# if "one of the girls" in playlist:
#     print("present")

# playlist[1]="see you again"
# print(playlist)

# order_summary=["pizza",2,500.00,True]
# print(order_summary)

# for index,item in enumerate(order_summary):
#     print(f"index: {index},Item:{item}")

#tupple_example=("apple","banana","orange",1)
# print(tupple_example[0])

#trip_summary=("uber","pondicherry","chennai airport",3500.00,"completed")
# print(trip_summary)
# trip_summary.append("150 kms")
# print(trip_summary)

# for item in trip_summary:
#     print(item)
    
# print(len(trip_summary))

# myd={"key1":"value1","key2":"value2","key3":"value"}
# print(myd)

# trip={
#     "provider":"uber",
#     "source":"pondicherry",
#     "destination":"chennai",
#     "fare":3500.00
# }
# print(trip["provider"])
# print(trip.get(3500.00))
# print(trip.keys())
# print(trip.values())

# for key,value in trip.items():
#     print(f"key:{key},value:{value}")
    
# trip.update({"distance":150})
# print(trip)

# trip.pop("distance")
# print(trip)

# trip["fare"]=4000.00
# print(trip)

#uber_cities1={"chennai","bangalore","hyderabad","delhi"}
# print(uber_cities)
# uber_cities.add("pondicherry")
# print(uber_cities)
# list_cities=list(uber_cities)
# print(type(list_cities))
# uber_cities2={"mumbai","kolkata","delhi","chennai"}
# print(uber_cities1.union(uber_cities2))
# print(uber_cities1.intersection(uber_cities2))
# print(uber_cities1.difference(uber_cities2))
# uber_cities1.add("pune")
# print(uber_cities1)
# uber_cities2.remove("mumbai")
# print(uber_cities2)

add=lambda a,b:a+b
print(add(5,3))

numbers=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

data=[
    {"name":"Alice","age":30},
    {"name":"Pravallika","age":21},
    {"name":"charlie","age":35}
]
young=min(data,key=lambda x:x["age"]<30)
print(young)