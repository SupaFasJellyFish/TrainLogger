# TrainLogger
Records data about trains that travel near you.

This project is meant to take broadcasts from railroad defect detectors in the United States (specifically CSX for now) and
stores the data from these trains in a SQLite database. I live near a set of railroad tracks, and after the East Palestine
derailment incident, I started becoming more curious about the trains that go by my neighborhood. Good publicly-available tracking 
options exist for planes and boats, but not for trains, hence why I needed to make this.

Railroad defect detectors are automated, fixed pieces of equipment that monitor many data points about trains that go by. 
They are necessary becausea train conductor can't monitor these on their own because the median length of trains in the US is 1 mile. 
This equipment measures the temperature of every wheel bearing, and checks for dragging bits. It then reports all of this data to
the conductor via a publicly available radio broadcast. with an SDR, this can be listened to, and with a speech-to-text engine,
turned into a string that can be parsed for the data of interest.
