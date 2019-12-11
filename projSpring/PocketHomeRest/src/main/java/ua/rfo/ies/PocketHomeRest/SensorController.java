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
public class SensorController {
	@Autowired
	private SensorRepository sensrepo;
	
	@GetMapping("/{house_id}/sensors")
	public List<Sensor> getSensorsByRoom(@PathVariable(value = "house_id") Long houseId){
		return sensrepo.findByhouseId(houseId);
	}
	
	@GetMapping("/sensors")
	public List<Sensor> getAllSensors(){
		return sensrepo.findAll();
	}
	
	@GetMapping("/sensors/{id}")
	public Sensor getSensor(@PathVariable(value = "id") Long Id){
		return sensrepo.findById(Id).get();
	}
	
	@PostMapping("/sensors")
	public Sensor createSensor(@Valid @RequestBody Sensor sensor) {
		return sensrepo.save(sensor);
	}
	
	// Não há delete porque ninguém retira sensores do sistema
	

}
