package ua.rfo.ies.PocketHomeRest;

import java.util.List;
import org.springframework.web.bind.annotation.RequestParam;


import javax.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.util.*;

@RestController
public class LogController {
	@Autowired
	private LogRepository logrepo;
	
	@GetMapping("/logs/{house_id}/{sensor_id}")
	public List<SensorLog> getSensorsByHouseAndSensor(@PathVariable(value = "house_id") Long houseId, @PathVariable(value = "sensor_id") Long sensorId){
		return logrepo.findByhouseIdAndSensorId(houseId,sensorId);
	}
	
	@GetMapping("/logs")
	public List<SensorLog> getAllLogs(){
		return logrepo.findAll();
	}
	
	@GetMapping("/logs/{id}")
	public SensorLog getLog(@PathVariable(value = "id") Long Id){
		return logrepo.findById(Id).get();
	}
	
	@PostMapping("/logs")
	public SensorLog createLog(@Valid @RequestBody SensorLog log) {
		return logrepo.save(log);
	}

	@PostMapping("/logs_light")
	public String insertLog(@Valid @RequestParam(name = "value")int value) {
		System.out.println("ola");
		System.out.println(value);
		//return logrepo.save(log);
		return "redirect:/dashboard";
	}


	// Não há put porque ninguém edita registos
	

}
