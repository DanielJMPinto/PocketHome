package com.PocketHome.model;


import java.util.Date;

import javax.persistence.*;

@Entity
@Table(name = "sensor_logs")
public class SensorLog {
	private long id;
	private Date date;
	private long sensorId;
	private String sensorType;
	private long roomId;

	public SensorLog(long id, Date date, long sensorId, String sensorType, long roomId) {
		super();
		this.id = id;
		this.date = date;
		this.sensorId = sensorId;
		this.sensorType = sensorType;
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

	@Column(name = "room_id", nullable = false)
	public long getRoomId() {
		return roomId;
	}

	public void setRoomId(long roomId) {
		this.roomId = roomId;
	}






}
