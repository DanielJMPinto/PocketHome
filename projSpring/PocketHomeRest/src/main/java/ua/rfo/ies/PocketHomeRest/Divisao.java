package ua.rfo.ies.PocketHomeRest;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.*;

@Entity
@Table(name = "rooms")
public class Divisao {
	private long id;
	private String alias;
	private long houseId;
	
	/*
	@OneToMany(mappedBy = "roomId")
	private List<Sensor> sensors = new ArrayList<>();
	*/
	
	public Divisao() {}

	public Divisao(long id, String alias, long houseId) {
		this.id = id;
		this.alias = alias;
		this.houseId = houseId;
	}
	
	/*
	public void updateSensors(Sensor sensor) {
		this.sensors.add(sensor);
		sensor.setRoom(this);
	}
	*/
	
	
	@Column(name = "house_id", nullable = false)
	public long getHouseId() {
		return houseId;
	}

	public void setHouseId(long houseId) {
		this.houseId = houseId;
	}

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "alias", nullable = false)
	public String getAlias() {
		return alias;
	}

	public void setAlias(String alias) {
		this.alias = alias;
	}
	
	
	
	
	
	

}
