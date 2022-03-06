from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from job_portal.service import \
    create_context_main, create_context_all_vacancy, context_vacancy_one_category_or_404, \
    context_one_companies_or_404, context_one_vacancy_or_404


def main(request):

    return render(
        request,
        'job_portal/index.html',
        context=create_context_main()
        )


def vacancies(request):

    return render(
        request,
        'job_portal/vacancies.html',
        context=create_context_all_vacancy()
        )


def category(request, cat):

    return render(
        request,
        'job_portal/vacancies.html',
        context=context_vacancy_one_category_or_404(cat)
        )


def companies(request, id):

    return render(
        request,
        'job_portal/company.html',
        context=context_one_companies_or_404(id)
        )


def selected_vacancy(request, id):

    return render(
        request,
        'job_portal/vacancy.html',
        context=context_one_vacancy_or_404(id)
        )


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
