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
    public partial class AlertCMethod2Linear : IEquatable<AlertCMethod2Linear>
    {
        /// <summary>
        /// Gets or Sets AlertCLocationCountryCode
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationCountryCode", EmitDefaultValue=false)]
        public string AlertCLocationCountryCode { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLocationTableNumber
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationTableNumber", EmitDefaultValue=false)]
        public string AlertCLocationTableNumber { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLocationTableVersion
        /// </summary>
        [Required]
        [MaxLength(1024)]
        [DataMember(Name="alertCLocationTableVersion", EmitDefaultValue=false)]
        public string AlertCLocationTableVersion { get; set; }

        /// <summary>
        /// Gets or Sets AlertCDirection
        /// </summary>
        [Required]
        [DataMember(Name="alertCDirection", EmitDefaultValue=false)]
        public AlertCDirection AlertCDirection { get; set; }

        /// <summary>
        /// Gets or Sets AlertCMethod2PrimaryPointLocation
        /// </summary>
        [Required]
        [DataMember(Name="alertCMethod2PrimaryPointLocation", EmitDefaultValue=false)]
        public AlertCMethod2PrimaryPointLocation AlertCMethod2PrimaryPointLocation { get; set; }

        /// <summary>
        /// Gets or Sets AlertCMethod2SecondaryPointLocation
        /// </summary>
        [Required]
        [DataMember(Name="alertCMethod2SecondaryPointLocation", EmitDefaultValue=false)]
        public AlertCMethod2SecondaryPointLocation AlertCMethod2SecondaryPointLocation { get; set; }

        /// <summary>
        /// Gets or Sets AlertCLinearExtensionG
        /// </summary>
        [DataMember(Name="alertCLinearExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> AlertCLinearExtensionG { get; set; }

        /// <summary>
        /// Gets or Sets AlertCMethod2LinearExtensionG
        /// </summary>
        [DataMember(Name="alertCMethod2LinearExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> AlertCMethod2LinearExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AlertCMethod2Linear {\n");
            sb.Append("  AlertCLocationCountryCode: ").Append(AlertCLocationCountryCode).Append("\n");
            sb.Append("  AlertCLocationTableNumber: ").Append(AlertCLocationTableNumber).Append("\n");
            sb.Append("  AlertCLocationTableVersion: ").Append(AlertCLocationTableVersion).Append("\n");
            sb.Append("  AlertCDirection: ").Append(AlertCDirection).Append("\n");
            sb.Append("  AlertCMethod2PrimaryPointLocation: ").Append(AlertCMethod2PrimaryPointLocation).Append("\n");
            sb.Append("  AlertCMethod2SecondaryPointLocation: ").Append(AlertCMethod2SecondaryPointLocation).Append("\n");
            sb.Append("  AlertCLinearExtensionG: ").Append(AlertCLinearExtensionG).Append("\n");
            sb.Append("  AlertCMethod2LinearExtensionG: ").Append(AlertCMethod2LinearExtensionG).Append("\n");
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
            return obj.GetType() == GetType() && Equals((AlertCMethod2Linear)obj);
        }

        /// <summary>
        /// Returns true if AlertCMethod2Linear instances are equal
        /// </summary>
        /// <param name="other">Instance of AlertCMethod2Linear to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AlertCMethod2Linear other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    AlertCLocationCountryCode == other.AlertCLocationCountryCode ||
                    AlertCLocationCountryCode != null &&
                    AlertCLocationCountryCode.Equals(other.AlertCLocationCountryCode)
                ) && 
                (
                    AlertCLocationTableNumber == other.AlertCLocationTableNumber ||
                    AlertCLocationTableNumber != null &&
                    AlertCLocationTableNumber.Equals(other.AlertCLocationTableNumber)
                ) && 
                (
                    AlertCLocationTableVersion == other.AlertCLocationTableVersion ||
                    AlertCLocationTableVersion != null &&
                    AlertCLocationTableVersion.Equals(other.AlertCLocationTableVersion)
                ) && 
                (
                    AlertCDirection == other.AlertCDirection ||
                    AlertCDirection != null &&
                    AlertCDirection.Equals(other.AlertCDirection)
                ) && 
                (
                    AlertCMethod2PrimaryPointLocation == other.AlertCMethod2PrimaryPointLocation ||
                    AlertCMethod2PrimaryPointLocation != null &&
                    AlertCMethod2PrimaryPointLocation.Equals(other.AlertCMethod2PrimaryPointLocation)
                ) && 
                (
                    AlertCMethod2SecondaryPointLocation == other.AlertCMethod2SecondaryPointLocation ||
                    AlertCMethod2SecondaryPointLocation != null &&
                    AlertCMethod2SecondaryPointLocation.Equals(other.AlertCMethod2SecondaryPointLocation)
                ) && 
                (
                    AlertCLinearExtensionG == other.AlertCLinearExtensionG ||
                    AlertCLinearExtensionG != null &&
                    other.AlertCLinearExtensionG != null &&
                    AlertCLinearExtensionG.SequenceEqual(other.AlertCLinearExtensionG)
                ) && 
                (
                    AlertCMethod2LinearExtensionG == other.AlertCMethod2LinearExtensionG ||
                    AlertCMethod2LinearExtensionG != null &&
                    other.AlertCMethod2LinearExtensionG != null &&
                    AlertCMethod2LinearExtensionG.SequenceEqual(other.AlertCMethod2LinearExtensionG)
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
                    if (AlertCLocationCountryCode != null)
                    hashCode = hashCode * 59 + AlertCLocationCountryCode.GetHashCode();
                    if (AlertCLocationTableNumber != null)
                    hashCode = hashCode * 59 + AlertCLocationTableNumber.GetHashCode();
                    if (AlertCLocationTableVersion != null)
                    hashCode = hashCode * 59 + AlertCLocationTableVersion.GetHashCode();
                    if (AlertCDirection != null)
                    hashCode = hashCode * 59 + AlertCDirection.GetHashCode();
                    if (AlertCMethod2PrimaryPointLocation != null)
                    hashCode = hashCode * 59 + AlertCMethod2PrimaryPointLocation.GetHashCode();
                    if (AlertCMethod2SecondaryPointLocation != null)
                    hashCode = hashCode * 59 + AlertCMethod2SecondaryPointLocation.GetHashCode();
                    if (AlertCLinearExtensionG != null)
                    hashCode = hashCode * 59 + AlertCLinearExtensionG.GetHashCode();
                    if (AlertCMethod2LinearExtensionG != null)
                    hashCode = hashCode * 59 + AlertCMethod2LinearExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(AlertCMethod2Linear left, AlertCMethod2Linear right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(AlertCMethod2Linear left, AlertCMethod2Linear right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
