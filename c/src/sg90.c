#include "pico/stdlib.h"
#include "hardware/pwm.h"

// pwm_frq = clk_frq / {(wrap + 1) * clkdiv}
uint slice_gpio_0;
uint wrap = 65025; 
float clkdiv = 38.45;
float angle_min = 0.025;
float angle_middle = 0.0725;
float angle_max = 0.12;

void sg90_init() {
    // Tell GPIO 0 is allocated to the PWM
    gpio_set_function(0, GPIO_FUNC_PWM);

    // Find out which PWM slice is connected to GPIO 0
    slice_gpio_0 = pwm_gpio_to_slice_num(0);

    // Set PWM clock divider in a PWM configuration
    pwm_set_clkdiv(slice_gpio_0, clkdiv);

    // Set the current PWM counter wrap value
    pwm_set_wrap(slice_gpio_0, wrap);

    // Initialise a PWM with settings from a configuration object
    pwm_set_enabled(slice_gpio_0, true);  
}

void sg90_set_angle(float angle) {
    float duty = angle_min + (angle_max - angle_min) / 180 * angle;
    pwm_set_chan_level(slice_gpio_0, PWM_CHAN_A, (uint16_t)(duty * wrap));
}