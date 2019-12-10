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
public class LogController {
	@Autowired
	private LogRepository logrepo;
	
	@GetMapping("/logs/{room_id}/{sensor_id}")
	public List<SensorLog> getSensorsByRoomAndSensor(@PathVariable(value = "room_id") Long roomId, @PathVariable(value = "sensor_id") Long sensorId){
		return logrepo.findByroomIdAndsensorId(roomId,sensorId);
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
	
	// Não há put porque ninguém edita registos
	

}
