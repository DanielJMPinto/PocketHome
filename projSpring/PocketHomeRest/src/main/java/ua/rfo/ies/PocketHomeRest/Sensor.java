package ua.rfo.ies.PocketHomeRest;


import javax.persistence.*;

@Entity
@Table(name = "sensors")
public class Sensor {
	private long id;
	private String type;
	private long roomId;

	public Sensor(long id, String type, long roomId) {
		super();
		this.id = id;
		this.type = type;
		this.roomId = roomId;
	}
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "room_id", nullable = true)
	public long getRoomId() {
		return roomId;
	}

	public void setRoomId(long roomId) {
		this.roomId = roomId;
	}

	@Column(name = "type", nullable = false)
	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}
	
	
	
	

}
