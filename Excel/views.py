from django.shortcuts import render
from .models import StudenData,Student
import xlrd
from django.core.files.storage import FileSystemStorage

"""
# Create your views here.
book = xlrd.open_workbook(os.path.join("D:\sikandar","Testd.xlsx"))
sheet = book.sheet_by_index(0)

database=pymysql.connect(
				host='localhost',
				user='root',
				password='',
				db='sikandar',
				charset='utf8mb4'
		)

cursor=database.cursor()

que="insert into xlsdf (name,Adds,Mobile) values(%s,%s,%s)"


for r in range(1,sheet.nrows):
	name=sheet.cell(r,1).value
	add=sheet.cell(r,2).value
	no=sheet.cell(r,3).value

	values=(name,add,no)

	cursor.execute(que,values)


cursor.close()

database.commit()

database.close()

print("all Record inserted")

"""



def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        book = xlrd.open_workbook(uploaded_file_url)
        sheet = book.sheet_by_index(0)
        for r in range(1, sheet.nrows):
            st_id=sheet.cell(r, 0).value
            st_name=sheet.cell(r,1).value
            st_add=sheet.cell(r,2).value
            st_st=sheet.cell(r,3).value
            st_per=sheet.cell(r,4).value


            std=Student.objects.create(st_id=st_id,st_name=st_name,st_add=st_add,st_st=st_st,st_per=st_per)
            std.save()

        return render(request, 'Excel/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'Excel/index.html')
