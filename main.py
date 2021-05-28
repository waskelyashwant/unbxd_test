import json
import requests
import csv

base_url1 = 'https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&amp;q=*&amp;rows=10&amp;start=0'
base_url2 = 'https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&amp;q=*&amp;rows=10&amp;start=1'


def lts(data,k):
	list_to_set=set(data)
	set_to_list=list(list_to_set)
	if k=='unbxd_color_for_category':
		a=[]
		for i in set_to_list:
			s=""
			for j in i:
				if j==':':
					break
				s+=j

			a.append(s)
		output=[str(x) for x in a]
		str1=","
		return str1.join(output)

		return
	output = [str(x) for x in set_to_list]
	str1 = ","
	return str1.join(output)


def main(data,m):
	s=set()
	for data0 in data:
		for k in data0.keys():
			s.add(k)

	fieldnames = list(s)

	f = open('Unbxd-2021-interns test_Yashwant_Singh_Waskel_' + m +'.csv', 'w')
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()


	for data0 in data:
		for k in data0.keys():
			if type(data0[k])==list:
				string = lts(data0[k],k)
				data0[k]=string
				# print(string)
			if type(data0[k])==bool:
				# print(k)
				# print(data0[k])
				if data0[k]==True:
					data0[k]='YES'
				elif data0[k]==False:
					data0[k]='NO'

	for row_dict in data:
		writer.writerow(row_dict)

	f.close()




x = requests.get(base_url1).json()

data1=[]
data2=[]
for i in x['response']['products']:
	data1.append(i)

main(data1,'0')

y = requests.get(base_url2).json()

for i in x['response']['products']:
	data2.append(i)

main(data2,'1')