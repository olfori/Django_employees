from django.http import JsonResponse

lsb='id'    # global variable last sort_by

def json_data_table(queryset, server_response):
    li = {'q': [], 's_res': server_response, 'p': []}    # packing data for json
    for emp in queryset:
        li['q'].append({
            'id': emp.id, 'nm': emp.name, 'pos': emp.position,
            'dt': emp.emp_date, 'sl': emp.salary,
            'url': emp.photo_thumbnail.url, 'par': emp.parent_id
        })
    li['p'].append({
        'has_prev': queryset.has_previous(), 'has_next': queryset.has_next(),
        'num_pages': queryset.paginator.num_pages, 'number': queryset.number,
        'count': queryset.paginator.count
    })
    print(li['p'])
    return JsonResponse(li)


def json_data_tree(queryset):
    li = {'q': []}
    for emp in queryset:
        li['q'].append({'id': emp.id, 'nm': emp.name, 'pos': emp.position,
                        'lev': emp.level, 'leaf': emp.is_leaf_node()})

    return JsonResponse(li)

# Remember last sort
def last_sort_by(sort_by=''):
    global lsb
    if sort_by:
        lsb = sort_by
    return lsb
