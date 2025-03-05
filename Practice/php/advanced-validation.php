<?php
/**
 * Validates an associative array of inputs based on provided rules.
 * Rules format: ['field_name' => ['required' => true, 'type' => 'email', 'min_length' => 5]]
 *
 * @param array $data
 * @param array $rules
 * @return array An array of error messages. Empty if valid.
 */
function validate_inputs(array $data, array $rules) {
    $errors = [];
    foreach ($rules as $field => $constraints) {
        $value = trim($data[$field] ?? '');
        // Check required
        if (!empty($constraints['required']) && $value === '') {
            $errors[$field][] = "$field is required.";
        }
        // Check type: email
        if (!empty($constraints['type']) && $constraints['type'] === 'email' && !filter_var($value, FILTER_VALIDATE_EMAIL)) {
            $errors[$field][] = "$field must be a valid email address.";
        }
        // Check minimum length
        if (!empty($constraints['min_length']) && strlen($value) < $constraints['min_length']) {
            $errors[$field][] = "$field must be at least {$constraints['min_length']} characters long.";
        }
    }
    return $errors;
}

// Example usage:
$data = [
    'username' => 'john',
    'email' => 'invalid-email'
];
$rules = [
    'username' => ['required' => true, 'min_length' => 5],
    'email' => ['required' => true, 'type' => 'email']
];
$errors = validate_inputs($data, $rules);
print_r($errors);
?>
