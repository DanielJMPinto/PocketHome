package ua.rfo.ies.PocketHomeRest;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LogRepository extends JpaRepository<SensorLog, Long>{
	List<SensorLog> findByhouseIdAndSensorId(long houseId, long sensorId);
	
	SensorLog findById(long id);

}
