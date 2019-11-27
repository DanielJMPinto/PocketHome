package ua.rfo.ies.PocketHomeRest;

import javax.persistence.*;

@Entity
@Table(name = "houses")
public class Casa {
	private long id;
	private String address;
	private String alias;
	
	@ManyToOne
	@JoinColumn(name = "owner_id")
	private User ownerId;
	
	public Casa() {}
	
	public Casa(long id, String address, String alias) {
		this.id = id;
		this.address = address;
		this.alias = alias;
	}

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
		public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
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
