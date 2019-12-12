package ua.rfo.ies.PocketHomeRest;


import java.util.Date;

import javax.persistence.*;

@Entity
@Table(name = "sensor_logs")
public class SensorLog {
	private long id;
	private Date date;
	private long sensorId;
	private String sensorType;
	private long value;
	private long houseId;

	public SensorLog(long id, Date date, long sensorId, String sensorType, long houseId, long value) {
		super();
		this.id = id;
		this.date = date;
		this.sensorId = sensorId;
		this.sensorType = sensorType;
		this.houseId = houseId;
		this.value = value;
	}
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "date", nullable = false)
	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}
	
	@Column(name = "sensor_id", nullable = false)
	public long getSensorId() {
		return sensorId;
	}

	public void setSensorId(long sensorId) {
		this.sensorId = sensorId;
	}
	
	@Column(name = "sensor_type", nullable = false)
	public String getSensorType() {
		return sensorType;
	}

	public void setSensorType(String sensorType) {
		this.sensorType = sensorType;
	}
	
	@Column(name = "house_id", nullable = false)
	public long getHouseId() {
		return houseId;
	}

	public void setHouseId(long houseId) {
		this.houseId = houseId;
	}
	
	@Column(name = "value", nullable = false)
	public long getValue() {
		return value;
	}

	public void setValue(long value) {
		this.value = value;
	}
	
	
	
	
	
	
	

}
