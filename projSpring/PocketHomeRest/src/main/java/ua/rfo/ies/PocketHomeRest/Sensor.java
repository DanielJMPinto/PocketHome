package ua.rfo.ies.PocketHomeRest;


import javax.persistence.*;

@Entity
@Table(name = "sensors")
public class Sensor {
	private long id;
	private String type;
	private long houseId;

	public Sensor(long id, String type, long houseId) {
		super();
		this.id = id;
		this.type = type;
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
	
	@Column(name = "house_id", nullable = true)
	public long getHouseId() {
		return houseId;
	}

	public void setHouseId(long houseId) {
		this.houseId = houseId;
	}

	@Column(name = "type", nullable = false)
	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}
	
	
	
	

}
