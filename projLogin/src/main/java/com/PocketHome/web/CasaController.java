package com.PocketHome.web;

import java.util.List;

import javax.validation.Valid;
import com.PocketHome.model.Casa;
import com.PocketHome.repository.CasaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
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

}
