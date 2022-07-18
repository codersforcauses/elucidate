# InputField

Provides a standard text box for use in forms.
It features validation, a label & a password variant.

## Props

- `fieldName`
    - Specifies the label text.
    - String.
    - Optional.
    - 'Field'
- `fieldType`
    - Specifies the HTML type attribute of the input.
    - String.
    - Optional.
    - 'text'
- `id`
    - Specifies the vee-validate ID for the inbuilt validation provider.
    - String.
    - Optional.
    - No default value.
- `rules`
    - Specifies the validation rules to apply. Can be one or more of the following:
        - `email` Ensures the value is an email address.
        - `required` Ensures the value is not null.
        - `min:length` Ensures the value is at least `length` characters long.
        - `password:target` Ensures the value matches the argument `target`.
    - String.
    - Optional.
    - No default value.

## Events

None.

## Slots

None.
