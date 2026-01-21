charge_options = {
    0: ["self.ui.lb_system_limit", "self.ui.chk_system_limit"],
    1: ["self.ui.lb_custom_limit", "self.ui.le_custom_limit"],
    2: ["self.ui.lb_disable_limit", "self.ui.chk_disable_limit"],
}

for key, value in charge_options.items():
    for widget in value:
        print(key, widget)