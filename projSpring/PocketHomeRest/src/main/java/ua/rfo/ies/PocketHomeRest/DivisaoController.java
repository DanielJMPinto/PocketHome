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
	private DivisaoRepository divisaorepo;
	
	@GetMapping("/{house_id}/rooms")
	public List<Divisao> getRoomsByHouse(@PathVariable(value = "house_id") Long houseId){
		return divisaorepo.findByhouseId(houseId);
	}
	
	@GetMapping("/rooms")
	public List<Divisao> getAllRooms(){
		return divisaorepo.findAll();
	}
	
	@GetMapping("/rooms/{id}")
	public Divisao getRoom(@PathVariable(value = "id") Long Id){
		return divisaorepo.findById(Id).get();
	}
	
	@PostMapping("/rooms")
	public Divisao createRoom(@Valid @RequestBody Divisao room) {
		return divisaorepo.save(room);
	}
	

}
