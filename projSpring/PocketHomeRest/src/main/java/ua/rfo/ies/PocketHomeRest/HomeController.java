package ua.rfo.ies.PocketHomeRest;

import ua.rfo.ies.PocketHomeRest.HomeService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("banana", "valor");
        System.out.println("banana");
        return "index";
    }

    @GetMapping(value = "/index")
    public String index(Model model, HomeService HomeService) {

        //var index = HomeService.all();
        // model.addAttribute("index", index);

        return "index";
    }

    @GetMapping("/pgFixe")
    @ResponseBody
    public String fixe(Model model){
        return "<h1>ola</h1>";
    }
}