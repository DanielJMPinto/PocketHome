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
        model.addAttribute("sensor_log_door", homeservice.find_sensor_log(0));
        model.addAttribute("sensor_log_flame", homeservice.find_sensor_log(1));
        model.addAttribute("sensor_log_gas", homeservice.find_sensor_log(2));
        model.addAttribute("sensor_log_hum_plants", homeservice.find_sensor_log(3));
        model.addAttribute("sensor_log_light", homeservice.find_sensor_log(4));
        model.addAttribute("sensor_log_motion", homeservice.find_sensor_log(5));
        model.addAttribute("sensor_log_rain", homeservice.find_sensor_log(6));
        model.addAttribute("sensor_log_sound", homeservice.find_sensor_log(7));
        model.addAttribute("sensor_log_temp", homeservice.find_sensor_log(8));
        model.addAttribute("sensor_log_hum", homeservice.find_sensor_log(9));
        model.addAttribute("sensor_log_knock", homeservice.find_sensor_log(10));

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

<<<<<<< HEAD
=======

    @GetMapping("/pgFixe")
    @ResponseBody
    public String fixe(Model model){
        return "<h1>ola</h1>";
    }
>>>>>>> 91013bd7aaa2249739fc9f63dcfd8805236b4455
}
