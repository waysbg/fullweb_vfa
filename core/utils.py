from django.views import generic as views


default_paginate_by = 25


class SearchBarView(views.ListView):

    def __get_start_date_search(self):
        start_date_search = self.request.GET.get('start_date_search', None)
        return start_date_search if start_date_search else ''

    def __get_end_date_search(self):
        end_date_search = self.request.GET.get('end_date_search', None)
        return end_date_search if end_date_search else ''

    def __get_description_search(self):
        description_search = self.request.GET.get('description_search', None)
        return description_search if description_search else ''

    def __get_start_amount_search(self):
        start_amount_search = self.request.GET.get('start_amount_search', None)
        return start_amount_search if start_amount_search else ''

    def __get_end_amount_search(self):
        end_amount_search = self.request.GET.get('end_amount_search', None)
        return end_amount_search if end_amount_search else ''

    def get_queryset(self):
        query_set = super().get_queryset()

        start_date_search = self.__get_start_date_search()
        end_date_search = self.__get_end_date_search()
        description_search = self.__get_description_search()
        start_amount_search = self.__get_start_amount_search()
        end_amount_search = self.__get_end_amount_search()

        if start_date_search:
            query_set = query_set.filter(date__gte=start_date_search)
        if end_date_search:
            query_set = query_set.filter(date__lte=end_date_search)
        if description_search:
            query_set = query_set.filter(description__icontains=description_search.lower())
        if start_amount_search:
            query_set = query_set.filter(amount__gte=start_amount_search)
        if end_amount_search:
            query_set = query_set.filter(amount__lte=end_amount_search)

        if not self.request.user.is_staff:
            query_set = query_set.filter(user_id=self.request.user.pk)

        return query_set

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['start_date_search'] = self.__get_start_date_search()
        context['end_date_search'] = self.__get_end_date_search()
        context['description_search'] = self.__get_description_search()
        context['start_amount_search'] = self.__get_start_amount_search()
        context['end_amount_search'] = self.__get_end_amount_search()

        context['total_amount'] = sum(user.amount for user in self.object_list.all())

        context['staff_member'] = self.request.user.is_staff
        context['supper_user'] = self.request.user.is_superuser
        context['show_bars'] = True
        return context

    def get_paginate_by(self, queryset):
        global default_paginate_by
        default_paginate_by = self.request.GET.get('page_size', default_paginate_by)
        return default_paginate_by

