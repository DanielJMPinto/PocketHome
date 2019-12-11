package com.PocketHome.model;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.*;

@Entity
@Table(name = "rooms")
public class Divisao {
	private long id;
	private String alias;
	
	@ManyToOne
	@JoinColumn(name  = "house_id")
	private Casa houseId;
	
	@OneToMany(mappedBy = "roomId")
	private List<Sensor> sensors = new ArrayList<>();
	
	public Divisao() {}

	public Divisao(long id, String alias, Casa house) {
		this.id = id;
		this.alias = alias;
		house.updateRooms(this);
	}
	
	public void updateSensors(Sensor sensor) {
		this.sensors.add(sensor);
		sensor.setRoom(this);
	}
	
	public void setHouse(Casa house) {
		this.houseId = house;
	}
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
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
