/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
    /// <summary>
    /// 
    /// </summary>
    [DataContract]
    public partial class HeightCoordinate : IEquatable<HeightCoordinate>
    {
        /// <summary>
        /// Gets or Sets HeightValue
        /// </summary>
        [Required]
        [DataMember(Name="heightValue", EmitDefaultValue=true)]
        public decimal HeightValue { get; set; }

        /// <summary>
        /// Gets or Sets HeightType
        /// </summary>
        [DataMember(Name="heightType", EmitDefaultValue=false)]
        public HeightTypeEnumG HeightType { get; set; }

        /// <summary>
        /// Gets or Sets AltitudeConfidence
        /// </summary>
        [DataMember(Name="altitudeConfidence", EmitDefaultValue=false)]
        public AltitudeConfidence AltitudeConfidence { get; set; }

        /// <summary>
        /// Gets or Sets VerticalPositionAccuracy
        /// </summary>
        [DataMember(Name="verticalPositionAccuracy", EmitDefaultValue=false)]
        public PositionAccuracy VerticalPositionAccuracy { get; set; }

        /// <summary>
        /// Gets or Sets HeightCoordinateExtensionG
        /// </summary>
        [DataMember(Name="heightCoordinateExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> HeightCoordinateExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class HeightCoordinate {\n");
            sb.Append("  HeightValue: ").Append(HeightValue).Append("\n");
            sb.Append("  HeightType: ").Append(HeightType).Append("\n");
            sb.Append("  AltitudeConfidence: ").Append(AltitudeConfidence).Append("\n");
            sb.Append("  VerticalPositionAccuracy: ").Append(VerticalPositionAccuracy).Append("\n");
            sb.Append("  HeightCoordinateExtensionG: ").Append(HeightCoordinateExtensionG).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((HeightCoordinate)obj);
        }

        /// <summary>
        /// Returns true if HeightCoordinate instances are equal
        /// </summary>
        /// <param name="other">Instance of HeightCoordinate to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(HeightCoordinate other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    HeightValue == other.HeightValue ||
                    
                    HeightValue.Equals(other.HeightValue)
                ) && 
                (
                    HeightType == other.HeightType ||
                    HeightType != null &&
                    HeightType.Equals(other.HeightType)
                ) && 
                (
                    AltitudeConfidence == other.AltitudeConfidence ||
                    AltitudeConfidence != null &&
                    AltitudeConfidence.Equals(other.AltitudeConfidence)
                ) && 
                (
                    VerticalPositionAccuracy == other.VerticalPositionAccuracy ||
                    VerticalPositionAccuracy != null &&
                    VerticalPositionAccuracy.Equals(other.VerticalPositionAccuracy)
                ) && 
                (
                    HeightCoordinateExtensionG == other.HeightCoordinateExtensionG ||
                    HeightCoordinateExtensionG != null &&
                    other.HeightCoordinateExtensionG != null &&
                    HeightCoordinateExtensionG.SequenceEqual(other.HeightCoordinateExtensionG)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    
                    hashCode = hashCode * 59 + HeightValue.GetHashCode();
                    if (HeightType != null)
                    hashCode = hashCode * 59 + HeightType.GetHashCode();
                    if (AltitudeConfidence != null)
                    hashCode = hashCode * 59 + AltitudeConfidence.GetHashCode();
                    if (VerticalPositionAccuracy != null)
                    hashCode = hashCode * 59 + VerticalPositionAccuracy.GetHashCode();
                    if (HeightCoordinateExtensionG != null)
                    hashCode = hashCode * 59 + HeightCoordinateExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(HeightCoordinate left, HeightCoordinate right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(HeightCoordinate left, HeightCoordinate right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
