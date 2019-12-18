package ua.rfo.ies.PocketHomeRest;

import ua.rfo.ies.PocketHomeRest.HomeService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.beans.factory.annotation.Autowired;

@Controller
public class HomeController {

    @Autowired
    HomeService homeservice;

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("banana", "valor");

        return "index";
    }

    @GetMapping(value = "/index")
    public String index(Model model, HomeService HomeService) {
        return "index";
    }

    @GetMapping("/login")
    public String login(Model model) {
        model.addAttribute("banana", "valor");
        System.out.println("login");
        return "login";
    }

    @GetMapping(value = "/dashboard")
    public String dashboard( Model model) {
        // TEMPERATURE
        model.addAttribute("sensor_log_temp", homeservice.find_sensor_log(8));

        // GAS
        model.addAttribute("gas",homeservice.find_sensor_log(2));

        System.out.println("gas: " + (homeservice.find_sensor_log(2)).getClass().getSimpleName() + " - " + homeservice.find_sensor_log(2));

        if(homeservice.find_sensor_log(2).isEmpty()){
            System.out.println("NO GAS");
            model.addAttribute("gas_flag","no_gas");
        }
        else{
            System.out.println("GAS");
            model.addAttribute("gas_flag","gas");
        }

        return "dashboard";
    }

}