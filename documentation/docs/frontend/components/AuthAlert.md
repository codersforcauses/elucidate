# AuthAlert

A list of validation errors with a header in a red coloured box.
Hides if there aren't any errors.

## Props

- `errors`
    - An array of errors to be shown in the list.
    - Array[Error].
    - Required.

## Events

None.

## Slots

- Default.
    - The message shown above the error list.
    - Falls back to 'Please fix the following errors:'
