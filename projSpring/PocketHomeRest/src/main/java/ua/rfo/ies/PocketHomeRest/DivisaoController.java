package ua.rfo.ies.PocketHomeRest;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DivisaoController {
	@Autowired
	private DivisaoRepository divisaorepository;
	
	/*
	@GetMapping("/{house_id}/rooms")
	public ResponseEntity<Divisao> getRoomsByHouse(@PathVariable(value = "house_id") Long houseId){
		return true;
	}
	
	@PostMapping("/houses")
	public Casa createHouse(@Valid @RequestBody Casa house) {
		return divisaorepository.save(house);
	}*/
	

}
