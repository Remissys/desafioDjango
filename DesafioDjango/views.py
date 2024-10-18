from django.shortcuts import render

def home_view(request):
    return render(request, './main.html')

def image_view(request):
    return render(request, './image.html')

def table_view(request):
    import csv

    csv_file_path = 'DesafioDjango/alunos.csv'

    data = []

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    context = {
        'data': data
    }

    return render(request, './table.html', context)