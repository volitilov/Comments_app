// validation_form.js

// Делает проверку формы по следующим критериям:
// - имя, фамилия, email, комментарий являются обязательными
// - проверяет поле телефона
// - проверяет поле email
// - проверяет минимальную и максимальную длину данных


// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

var j = jQuery.noConflict();

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

j(function() {
    var form = j('form');
    var csrf_token = j('#csrf_token');
    var first_name = j('#first_name');
    var last_name = j('#last_name');
    var middle_name = j('#middle_name');
    var phone = j('#phone');
    var region = j('#region');
    var city = j('#city');
    var email = j('#email');
    var comment = j('#comment');

    var errors_msg = {
        'required': 'Это поле обязательно',
        'min_length': 'Слишком короткое',
        'max_length': 'Слишком длиное',
        'phone': 'Не является телефоном: пример формата +375 33 6157799',
        'email': 'Не является почтовым ящиком: пример формата my_mail@mail.ru'
    }
    var max_value_length = 50;
    var min_value_length = 3;
    var max_value_comment_length = 1000;


    var phone_regex = /^(\+\d{3})?\d{9}$/;
    var email_regex = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    var required_fileds = [first_name, last_name, email, comment];
    var all_fields = required_fileds.concat([middle_name, phone, region, city, csrf_token]);
    var data_state = false;


    function addError_field(field, er_msg) {
        // добавляет ошибку к полю, где:
        // - field - поле на которую вешается ошибка
        // - er_msg - текст ошибки
        var form_group = field.parent().parent();
        form_group.addClass('errored');
        form_group.append('<dd class="error">'+er_msg+'</dd>');
        field.css({'border-color': 'red'});
    }

    function removeError_field(field) {
        // удаляет ошибку у указыного поля, где:
        // - field - поле у которого надо удалить ошибку
        var form_group = field.parent().parent();
        form_group.removeClass('errored');
        field.css({'border-color': ''});
    }
    

    j(required_fileds.concat([phone])).each(function(index, elem) {
        j(elem).focus(function() {
            // если на поле висит ошибка и пользователь захотел его
            // исправить то данный код удаляет ошибку у поля при
            // фокусе
            removeError_field(j(elem));
        });
    });

    form.submit(function(e) {
        data_state = true;
        j(required_fileds).each(function(index, elem) {
            if (elem.val() == '' && elem.val().length == 0) {
                // смотрит чтобы поле не было пустым, если условия 
                // нарушаются вешается соответствующая ошибка
                addError_field(elem, errors_msg['required']);
                data_state = false;
            }

            if (elem.val().length < min_value_length && elem.val().length != 0) {
                // смотрит чтобы длина была не меньше 3 символов иначе
                // вешается соответствующая ошибка
                addError_field(elem, errors_msg['min_length']);
                data_state = false;
            }

            if (elem.val().length > max_value_length && elem.prop('id') != 'comment') {
                // проверяет поле на максимальную длину, которая не 
                // должна привышать указанного значения, кромме комментарии
                // так как комментарий может быть гораздо больше
                addError_field(elem, errors_msg['max_length']);
                data_state = false;
            }

            if (elem.prop('id') == 'comment' && elem.val().length > max_value_comment_length) {
                // отдельно проверяет комментарий на максимальную длину
                addError_field(elem, errors_msg['max_length']);
                data_state = false;
            }
        });

        if ( !email_regex.test(email.val()) && email.val().length > 0 ) {
            // пропускаю email через регулярку
            addError_field(email, errors_msg['email']);
            data_state = false;
        }

        var phone_data = phone.val().replace(/\s+/g, '');
        if ( !phone_regex.test(phone_data) && phone.val().length > 0 ) {
            // пропускаю телефон через регулярку
            addError_field(phone, errors_msg['phone']);
            data_state = false;
        }


        if (data_state) {
            // если состояние проверки положительное, то формирую
            // необходимые данные для отправки
            var data = new FormData;
            j(all_fields).each(function(index, elem) {
                data.append(elem.prop('id'), elem.val());
            });

            // оправляю POST запрос с данными
            j.ajax({
                url: form.attr('action'),
                type: form.attr('method'),
                contentType: false,
                processData: false,
                data: data
            }).done(function(data) {
                // если получил от сервера редирект, то направляю
                // пользователя далее.
                if (data['next_url']) {
                    window.location.replace(data['next_url']);
                }
            }).fail(function(data) {
                console.log(data);
            });

        }

        e.preventDefault();
    })
})
