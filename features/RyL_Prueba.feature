Feature: Quiero registrarme y logearme en el sitio web para acceder a los servicios

Scenario: Registro exitoso
    Given Abro el navegador
    When Ingreso a la página de registro
    And Selecciono la opcion Register
    And Diligencio el campo Login identificado con el selector "#username" con el valor "RamiroVelasquez"
    And Diligencio el campo First Name identificado con el selector "#firstName" con el valor "Oscar"
    And Diligencio el campo Last Name identificado con el selector "#lastName" con el valor "Coredi"
    And Diligencio el campo Password identificado con el selector "#password" con el valor "Raminata123"
    And Diligencio el campo Confirm Password identificado con el selector "#confirmPassword" con el valor "Raminata123"        
    Then Hago clic en el boton Register
    And Diligencio el User identificado con el selector "input[placeholder='Login']" con el valor "RamiroVelasquez"
    And Diligencio el Password identificado con el selector "input[name='password']" con el valor "Raminata123"
    Then Hago clic en el botón Login
    # Then Veo la pantalla de inicio