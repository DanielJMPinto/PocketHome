package com.PocketHome.model;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.*;

@Entity
@Table(name = "houses")
public class Casa {
	private long id;
	private String address;
	private String alias;

	private long ownerId;

	@OneToMany(mappedBy = "houseId")
	private List<Divisao> rooms = new ArrayList<>();

	/*
	@ManyToOne
	@JoinColumn(name = "owner_id")
	private User owner;
	*/

	public Casa() {}

	public Casa(long id, String address, String alias, User owner) {
		this.id = id;
		this.address = address;
		this.alias = alias;
		//owner.updateHouses(this);
	}

	public void updateRooms(Divisao room) {
		this.rooms.add(room);
		room.setHouse(this);
	}

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}

	@Column(name = "owner_id", nullable = false)
	public long getOwnerId() {
		return ownerId;
	}

	public void setOwnerId(long ownerId) {
		this.ownerId = ownerId;
	}

	@Column(name = "address", nullable = false)
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}

	@Column(name = "alias", nullable = false)
	public String getAlias() {
		return alias;
	}

	public void setAlias(String alias) {
		this.alias = alias;
	}

	@Override
	public String toString() {
		return "Casa [id=" + id + ", address=" + address + ", alias=" + alias + "]";
	}





}
