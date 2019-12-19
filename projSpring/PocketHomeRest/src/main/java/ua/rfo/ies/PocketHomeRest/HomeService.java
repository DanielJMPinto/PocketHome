
package ua.rfo.ies.PocketHomeRest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Service;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Date;
import java.util.List;

@Service
public class HomeService{
    @Autowired
    JdbcTemplate template;

    public List<SensorLog> find_sensor_log(int id) {
        String sql = "select * from sensor_logs where sensor_id=" + id + " order by id desc limit 1;";
        RowMapper<SensorLog> rm = new RowMapper<SensorLog>() {
            @Override
            public SensorLog mapRow(ResultSet resultSet, int i) throws SQLException {
                SensorLog log = new SensorLog(resultSet.getLong("id"),
                        resultSet.getDate("date"),
                        resultSet.getLong("sensor_id"),
                        resultSet.getString("sensor_type"),
                        resultSet.getLong("house_id"),
                        resultSet.getLong("value"),
                        resultSet.getString("img")
                );
                return log;
            }
        };
        return template.query(sql, rm);
    }


    public List<SensorLog> getTenLatestReadings(int sensorId, String date){
        String sql = "select * from sensor_logs where sensor_id=" + sensorId + " order by date desc;";

        RowMapper<SensorLog> rm = new RowMapper<SensorLog>() {
            @Override
            public SensorLog mapRow(ResultSet resultSet, int i) throws SQLException {
                SensorLog log = new SensorLog(resultSet.getLong("id"),
                        resultSet.getDate("date"),
                        resultSet.getLong("sensor_id"),
                        resultSet.getString("sensor_type"),
                        resultSet.getLong("house_id"),
                        resultSet.getLong("value"),
                        resultSet.getString("img")
                );
                return log;
            }
        };
        return template.query(sql, rm);
    }

}