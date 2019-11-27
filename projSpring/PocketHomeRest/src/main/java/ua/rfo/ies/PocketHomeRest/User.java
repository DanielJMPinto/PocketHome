package ua.rfo.ies.PocketHomeRest;

import javax.persistence.*;
import java.util.List;

@Entity
@Table(name = "users")
public class User {
	private long id;
	private String firstName;
	private String lastName;
	private String email;
	private String password;
	
	@OneToMany(mappedBy = "ownerId")
	private List<Casa> houses;
	
	
	public User() {}

	public User(long id, String firstName, String lastName, String email, String password) {
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
		this.email = email;
		this.password = password;
	}
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
		public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	
	@Column(name = "first_name", nullable = false)
    public String getFirstName() {
        return firstName;
    }
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
 
    @Column(name = "last_name", nullable = false)
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
 
    @Column(name = "email_address", nullable = false)
    public String getEmailId() {
        return email;
    }
    public void setEmailId(String emailId) {
        this.email = emailId;
    }
    
    @Column(name = "password", nullable = false)
    public String getPassword() {
    	return password;
    }
    public void setPassword(String password) {
    	this.password = password;
    }

	@Override
	public String toString() {
		return "User [id=" + id + ", firstName=" + firstName + ", lastName=" + lastName + ", email=" + email
				+ ", password=" + password + "]";
	}
    
    
}
