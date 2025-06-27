import requests
from django.shortcuts import render

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get("result") == "success":
        rates = data.get("rates", {})
        rate = rates.get(to_currency)
        if rate:
            return round(amount * rate, 2)
    return None

def imt_calculator(request):
    # Здесь твой полный код обработки ИМТ без изменений
    result = None
    category = None
    color = None
    advice = None
    ideal_weight = None
    weight = None
    height = None
    error = None

    converted_amount = None
    conversion_error = None

    class_map = {
        "Недостаточный вес": "color-low",
        "Нормальный вес": "color-normal",
        "Избыточный вес": "color-overweight",
        "Ожирение": "color-obese",
    }

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "bmi":
            # Твой код обработки ИМТ (без изменений)
            try:
                weight = float(request.POST.get("weight"))
                height = float(request.POST.get("height"))

                if height <= 0 or weight <= 0:
                    error = "Рост и вес должны быть положительными числами."
                    color = "#dc3545"
                else:
                    height_m = height / 100
                    imt = weight / (height_m ** 2)
                    result = round(imt, 2)

                    if result < 18.5:
                        category = "Недостаточный вес"
                        color = "#ffc107"
                        advice = "Рекомендуется увеличить калорийность рациона и добавить физические упражнения для набора массы."
                    elif 18.5 <= result < 25:
                        category = "Нормальный вес"
                        color = "#28a745"
                        advice = "Отлично! Поддерживайте свой здоровый образ жизни."
                    elif 25 <= result < 30:
                        category = "Избыточный вес"
                        color = "#ffc107"
                        advice = "Рекомендуется пересмотреть диету и увеличить физическую активность."
                    else:
                        category = "Ожирение"
                        color = "#dc3545"
                        advice = "Обратитесь к врачу или диетологу для консультации и плана снижения веса."

                    ideal_weight_min = 18.5 * (height_m ** 2)
                    ideal_weight_max = 24.9 * (height_m ** 2)
                    ideal_weight = f"{round(ideal_weight_min, 1)} - {round(ideal_weight_max, 1)}"

            except (ValueError, TypeError):
                error = "Пожалуйста, введите корректные числовые значения для роста и веса."
                color = "#dc3545"

        elif form_type == "currency":
            # Новая обработка формы конвертации валют
            try:
                amount = float(request.POST.get("amount"))
                from_currency = request.POST.get("from_currency")
                to_currency = request.POST.get("to_currency")

                converted_amount = convert_currency(amount, from_currency, to_currency)
                if converted_amount is None:
                    conversion_error = "Ошибка при получении курса валют."
            except Exception as e:
                conversion_error = f"Проверьте введённые данные для конвертации. Ошибка: {str(e)}"

    context = {
        "bmi": result,
        "category": error if error else category,
        "color": color if color else "#007bff",
        "advice": None if error else advice,
        "ideal_weight": None if error else ideal_weight,
        "weight": weight if weight is not None else "",
        "height": height if height is not None else "",
        "category_class": class_map.get(category, ""),
        "converted_amount": converted_amount,
        "conversion_error": conversion_error,
    }

    return render(request, "calculator/index.html", context)
