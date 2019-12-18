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
        //System.out.println("banana2");
        //var index = HomeService.all();
        // model.addAttribute("index", index);

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
        model.addAttribute("sensor_log_temp", homeservice.find_sensor_log(8));

        return "dashboard";
    }

    @GetMapping("/pgFixe")
    @ResponseBody
    public String fixe(Model model){
        return "<h1>ola</h1>";
    }
}