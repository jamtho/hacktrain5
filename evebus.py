"""Event bus.

Persists messages in a single sqlite3 database file."""

import sqlite3


##  ======================================================================
##  Constants

EVEFILE_NAME = "events.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
    timestamp  INTEGER  NOT NULL,
    sensor     TEXT     NOT NULL,
    value      REAL     NOT NULL
);
"""


##  ======================================================================
##  Init file at module boot

with sqlite3.connect (EVEFILE_NAME) as conn:
    conn.executescript (SCHEMA)
    conn.commit ()


##  ======================================================================
##  Module API

def write (event):
    """Write an event to the DB. Must be a dict with timestamp, sensor,
    value keys"""
    conn = sqlite3.connect (EVEFILE_NAME)
    conn.execute ("""INSERT INTO events (timestamp, sensor, value)
                     VALUES (?, ?, ?)""",
                  (event["timestamp"], event["sensor"], event["value"]))
    conn.commit ()

def after (timestamp):
    """Return all events in the DB with stored timestamp after timestamp"""
    conn = sqlite3.connect (EVEFILE_NAME)
    rows = conn.execute ("""SELECT timestamp, sensor, value FROM events
                            WHERE timestamp > ?
                            ORDER BY timestamp ASC""",
                         (timestamp,)) .fetchall()
    def toDict (row):
        return {"timestamp": row[0], "sensor": row[1], "value": row[2]}
    return [toDict(row) for row in rows]

                        
