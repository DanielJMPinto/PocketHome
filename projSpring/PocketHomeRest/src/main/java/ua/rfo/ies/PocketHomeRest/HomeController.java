package ua.rfo.ies.PocketHomeRest;

import com.zetcode.service.WordService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MyController {

    @GetMapping(value = "/")
    public String home() {

        return "index";
    }

    @GetMapping(value = "/index")
    public String index(Model model, HomeService HomeService) {

        var index = HomeService.all();
        model.addAttribute("index", index);

        return "index";
    }
}