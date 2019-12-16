package ua.rfo.ies.PocketHomeRest;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CasaController {
	@Autowired
	private CasaRepository casarepository;
	
	@GetMapping("/houses")
	public List<Casa> getAllHouses() {
		return casarepository.findAll();
	}
	
	@PostMapping("/houses")
	public Casa createHouse(@Valid @RequestBody Casa house) {
		return casarepository.save(house);
	}
	
	@PutMapping(value = "/houses/{id}")
    Casa alterCasa (@RequestBody Casa newhouse, @PathVariable(value = "id") Long houseId){
        Casa house =  casarepository.findById(houseId).get();
        house.setAddress(newhouse.getAddress());
        house.setAlias(newhouse.getAlias());
        house.setOwnerId(newhouse.getOwnerId());
        return casarepository.save(house);
    }

}
