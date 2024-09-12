package org.openapitools.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonValue;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import javax.validation.Valid;
import javax.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import javax.annotation.Generated;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * Gets or Sets EmissionClassificationEuroEnum
 */

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2024-09-12T12:02:17.317314499Z[Etc/UTC]", comments = "Generator version: 7.8.0")
public enum EmissionClassificationEuroEnum {
  
  EURO5("euro5"),
  
  EURO5A("euro5a"),
  
  EURO5B("euro5b"),
  
  EURO6("euro6"),
  
  EURO6A("euro6a"),
  
  EURO6B("euro6b"),
  
  EURO6C("euro6c"),
  
  EURO_V("euroV"),
  
  EURO_VI("euroVI"),
  
  OTHER("other"),
  
  EXTENDED_G("extendedG");

  private String value;

  EmissionClassificationEuroEnum(String value) {
    this.value = value;
  }

  @JsonValue
  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  @JsonCreator
  public static EmissionClassificationEuroEnum fromValue(String value) {
    for (EmissionClassificationEuroEnum b : EmissionClassificationEuroEnum.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }
}

