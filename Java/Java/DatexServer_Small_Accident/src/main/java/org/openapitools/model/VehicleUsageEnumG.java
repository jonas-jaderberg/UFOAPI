package org.openapitools.model;

import java.net.URI;
import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import org.openapitools.model.VehicleUsageEnum;
import org.openapitools.jackson.nullable.JsonNullable;
import java.time.OffsetDateTime;
import javax.validation.Valid;
import javax.validation.constraints.*;
import io.swagger.v3.oas.annotations.media.Schema;


import java.util.*;
import javax.annotation.Generated;

/**
 * VehicleUsageEnumG
 */

@Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2024-09-12T12:02:17.317314499Z[Etc/UTC]", comments = "Generator version: 7.8.0")
public class VehicleUsageEnumG {

  private VehicleUsageEnum value;

  private String extendedValueG;

  public VehicleUsageEnumG() {
    super();
  }

  /**
   * Constructor with only required parameters
   */
  public VehicleUsageEnumG(VehicleUsageEnum value) {
    this.value = value;
  }

  public VehicleUsageEnumG value(VehicleUsageEnum value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @NotNull @Valid 
  @Schema(name = "value", requiredMode = Schema.RequiredMode.REQUIRED)
  @JsonProperty("value")
  public VehicleUsageEnum getValue() {
    return value;
  }

  public void setValue(VehicleUsageEnum value) {
    this.value = value;
  }

  public VehicleUsageEnumG extendedValueG(String extendedValueG) {
    this.extendedValueG = extendedValueG;
    return this;
  }

  /**
   * Get extendedValueG
   * @return extendedValueG
   */
  
  @Schema(name = "extendedValueG", requiredMode = Schema.RequiredMode.NOT_REQUIRED)
  @JsonProperty("extendedValueG")
  public String getExtendedValueG() {
    return extendedValueG;
  }

  public void setExtendedValueG(String extendedValueG) {
    this.extendedValueG = extendedValueG;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleUsageEnumG vehicleUsageEnumG = (VehicleUsageEnumG) o;
    return Objects.equals(this.value, vehicleUsageEnumG.value) &&
        Objects.equals(this.extendedValueG, vehicleUsageEnumG.extendedValueG);
  }

  @Override
  public int hashCode() {
    return Objects.hash(value, extendedValueG);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleUsageEnumG {\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    extendedValueG: ").append(toIndentedString(extendedValueG)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

