package ua.rfo.ies.PocketHomeRest;


import javax.persistence.*;

@Entity
@Table(name = "sensors")
public class Sensor {
	private long id;
	private String type;
	
	@ManyToOne
	@JoinColumn(name  = "room_id")
	private Divisao roomId;

	public Sensor(long id, String type, Divisao roomId) {
		super();
		this.id = id;
		this.type = type;
		roomId.updateSensors(this);
	}
	
	public void setRoom(Divisao roomId) {
		this.roomId = roomId;
	}
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "type", nullable = false)
	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}
	
	
	
	

}
