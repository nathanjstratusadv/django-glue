class GlueFormFieldBinder {
    constructor(glue_form_field, field_element) {
        this.glue_form_field = glue_form_field
        this.field_element = field_element
    }

    bind() {
        this.set_field_class()
        this.set_html_attrs()
        this.set_label()
    }

    get label() {
        return this.field_element.previousElementSibling
    }

    set_label() {
        let label = this.label
        label.classList.add('form-label')
        label.setAttribute('for', this.glue_form_field.id)
        label.innerText = this.glue_form_field.label
        if(this.glue_form_field.is_required()) {
            label.innerText = label.innerText + '*'
        }
    }

    set_field_class() {
        this.field_element.classList.add('form-control')
    }

    set_html_attrs() {
        for (let field_attr of this.glue_form_field.attrs) {
            this.field_element.setAttribute(field_attr.name, field_attr.value)
        }
    }
}


class GlueCheckboxFieldBinder extends GlueFormFieldBinder {

    set_label(label_element) {
        let label = this.label
        this.label.classList.add('form-check-label')
        label.setAttribute('for', this.glue_form_field.id)
        label.innerText = this.glue_form_field.label
        this._field_element.insertAdjacentElement('afterend', label)
    }

    set_field_class() {
        this._field_element.classList.add('form-check-input')
        this._field_element.classList.add('me-2')
    }
}


class GlueSelectFieldBinder extends GlueFormFieldBinder {
    add_option(key, value) {
        const option = document.createElement('option')
        option.value = key
        option.text = value
        this._field_element.appendChild(option)
    }

    bind() {
        super.bind()
        this._field_element.innerHTML = ''
        this.add_option(null, '----------------')

        this.glue_form_field.choices.forEach(choice => {
            this.add_option(choice[0], choice[1])
        })
    }
}


class GlueRadioFieldBinder extends GlueFormFieldBinder {

    add_radio_input(key, value, index) {
        let parent_div = document.createElement('div')
        parent_div.classList.add('form-check')

        let radio_input = this._field_element.cloneNode(true)
        let increment_id = `${radio_input.id}${index}`

        radio_input.setAttribute('id', increment_id)
        radio_input.setAttribute('value', key)

        let radio_label = this.label.cloneNode(true)
        radio_label.setAttribute('for', increment_id)
        radio_label.innerText = value

        parent_div.appendChild(radio_input)
        parent_div.appendChild(radio_label)

        this.label.insertAdjacentElement('beforebegin', parent_div)
    }

    bind() {
        // Adds attributes to label and field
        super.bind()

        // Duplicates label and field and appends to area
        this.glue_form_field.choices.forEach((choice, index) => {
            this.add_radio_input(choice[0], choice[1], index)
        })

        // Hide original label and field.
        this._field_element.classList.add('d-none')
        this.label.classList.add('d-none')
    }

    set_label() {
        super.set_label()
        this.label.classList.add('mb-0')
    }

    set_field_class() {
        this._field_element.classList.add('form-check-input')
        this._field_element.classList.add('me-2')
    }

}
