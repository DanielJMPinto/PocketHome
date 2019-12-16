package ua.rfo.ies.PocketHomeRest;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SensorRepository extends JpaRepository<Sensor, Long>{
	List<Sensor> findByhouseId(long houseId);
	
	Sensor findById(long id);

}
